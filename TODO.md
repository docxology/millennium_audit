# TODO

## Workflowz review — 2026-11-10

- [ ] **MA-001 — P1 — Make closed-theorem verdicts evidence-backed rather than unconditionally negative**
  - **Observable outcome:** A final with no recognized premise binders is no longer automatically labeled `OFF_TOPIC_THEOREM` and non-resolving. Preserve the six reviewed findings for the frozen artifact, but represent an unrecognized closed signature as requiring review (or resolve it positively only through an explicit statement-equivalence rule), instead of deriving a negative verdict merely from an empty premise list.
  - **Evidence:** `src/statement_audit.py:35-38` supplies only parser facts to classification; `src/statement_audit.py:56-68` handles premises but otherwise assigns `resolves = False` and `OFF_TOPIC_THEOREM`; `src/statement_audit.py:75-83` commits those values to the result. The public field description at `src/statement_audit.py:13` includes `PROVES`, and `tests/test_audit.py:82-84` verifies only the universal-negative outcome, so there is no positive or unreviewed path.
  - **Acceptance probe (run from the repository root):**
    ```sh
    python3 - <<'PY'
    import sys
    sys.path.insert(0, "src")
    import lean_parser
    from clay_statements import CLAY_STATEMENTS
    from statement_audit import StatementAuditor

    auditor = StatementAuditor(CLAY_STATEMENTS, lean_parser)
    text = "theorem hodge_kunneth : unreviewed_closed_statement := witness"
    verdicts = auditor.audit(text)
    hodge = next(v for v in verdicts if v.problem == "Hodge")
    assert hodge.verdict == "REVIEW_REQUIRED"
    assert not hodge.resolves_official_statement
    assert all(v.verdict != "OFF_TOPIC_THEOREM" for v in verdicts if v.theorem_kind is None)

    actual = (open("package/MillenniumLean/Millennium.lean").read())
    current = StatementAuditor(CLAY_STATEMENTS, lean_parser).audit(actual)
    assert {v.problem for v in current} == set(CLAY_STATEMENTS)
    assert next(v for v in current if v.problem == "Hodge").verdict == "OFF_TOPIC_THEOREM"
    PY
    python3 -m pytest tests/ -q
    ```
    The first synthetic case must not produce an unconditional `OFF_TOPIC_THEOREM`; the real frozen package must retain its reviewed Hodge classification.
  - **Dependencies/constraints:** Coordinate with MA-005 because parser facts must remain stable while lexical extraction improves. Do not infer mathematical proof merely from a name, a zero-binder header, or an unchecked string; any positive result requires an explicit, reviewable equivalence decision. Keep all changes outside the verbatim audited package (`AGENTS.md:3-7`).

- [ ] **MA-002 — P1 — Prevent alternate-package audits from clobbering the canonical report**
  - **Observable outcome:** The positional package argument remains supported, but a caller can direct its JSON to a separate `--output` path. An alternate-package run leaves `data/audit_report.json` byte-for-byte unchanged; the documented default invocation still writes the canonical report.
  - **Evidence:** Alternate input is explicitly documented at `scripts/run_audit.py:2-5` and read at `scripts/run_audit.py:24-26`, while `scripts/run_audit.py:81-82` always writes the same tracked path. README's command at `README.md:30-34` provides no separation for results from another package.
  - **Acceptance probe (run from the repository root):**
    ```sh
    tmp=$(mktemp -d)
    cp -R package/MillenniumLean "$tmp/MillenniumLean"
    cp data/audit_report.json "$tmp/before.json"
    python3 scripts/run_audit.py "$tmp/MillenniumLean" --output "$tmp/alternate.json"
    cmp -s data/audit_report.json "$tmp/before.json"
    python3 - "$tmp/alternate.json" <<'PY'
    import json, sys
    with open(sys.argv[1], encoding="utf-8") as handle:
        report = json.load(handle)
    assert len(report["verdicts"]) == 6
    assert report["inventory"]["Millennium.lean"]["sha256"]
    PY
    python3 scripts/run_audit.py --output "$tmp/default-input.json"
    test -s "$tmp/default-input.json"
    rm -rf "$tmp"
    ```
  - **Dependencies/constraints:** Add only orchestration/CLI plumbing; the audited package and its hashes are immutable. Preserve backward compatibility for one positional package path and document the new output option in the run instructions. If output covers a different artifact, retain enough input provenance in the JSON to distinguish it from the canonical report.

- [ ] **MA-003 — P2 — Make the machine-readable report test fail when its required evidence is absent**
  - **Observable outcome:** `test_report_json_written` loads and validates the required report unconditionally rather than silently succeeding on a missing file, while still passing with the checked-in report present.
  - **Evidence:** The entire assertion at `tests/test_audit.py:140-144` is guarded by `if report.exists()`, giving the test a zero-assertion success path. The report is produced only by the separate orchestrator at `scripts/run_audit.py:81-83`, so collection of the tests alone does not guarantee that the file exists.
  - **Acceptance probe (run from the repository root):**
    ```sh
    tmp=$(mktemp -d)
    mv data/audit_report.json "$tmp/audit_report.json"
    python3 -m pytest tests/test_audit.py::test_report_json_written -q
    missing_rc=$?
    mv "$tmp/audit_report.json" data/audit_report.json
    rmdir "$tmp"
    test "$missing_rc" -ne 0
    python3 -m pytest tests/test_audit.py::test_report_json_written -q
    ```
    Success means the missing-report invocation failed, restoration succeeded, and the present-report invocation passed.
  - **Dependencies/constraints:** Treat `data/audit_report.json` as the required checked-in artifact already listed in the repository inventory; do not make this unit test rewrite it or depend on test execution order. Any deeper schema/freshness validation is a separate change.

- [ ] **MA-004 — P2 — Restrict sorry detection to live Lean code**
  - **Observable outcome:** The scanner continues to find an actual sorry tactic but ignores sorry text inside Lean string literals and nested block comments, consistent with its stated “live sorry tactic” contract.
  - **Evidence:** `src/lean_parser.py:19-48` tracks only a Boolean block-comment state and therefore closes at the first `-/`, without nested-comment depth or string-literal state. `src/lean_parser.py:51-58` then applies `\bsorry\b` to every remaining line, despite describing results as live tactics.
  - **Acceptance probe (run from the repository root):**
    ```sh
    python3 - <<'PY'
    import sys
    sys.path.insert(0, "src")
    from lean_parser import extract_sorries

    nested_comment = "/- outer\n  /- inner -/\n  sorry\n-/"
    assert extract_sorries(nested_comment) == []
    assert extract_sorries('def label := "sorry"') == []
    live = extract_sorries("theorem t : True := by\n  sorry")
    assert live == [(2, "sorry")]
    PY
    python3 -m pytest tests/test_audit.py::test_no_live_sorry -q
    ```
  - **Dependencies/constraints:** Preserve line-number reporting and the existing public return shape. Handle escapes in strings and nested comments without modifying package sources. Keep multi-line Lean declarations/commands in mind while extending the lexer; do not “fix” this by removing all keyword detection.

- [ ] **MA-005 — P2 — Scan declarations and project axioms after comment stripping and with legal indentation**
  - **Observable outcome:** Indented declarations inside a namespace are counted, indented project axioms are reported, and declaration-looking text inside block comments is excluded from both inventories.
  - **Evidence:** `src/lean_parser.py:8-16` runs anchored regular expressions directly on the raw input; `^axiom` admits no indentation, and neither extractor calls the comment stripper defined at `src/lean_parser.py:19-48`. These results drive the printed kernel-hygiene totals at `scripts/run_audit.py:39-43` and the assertions at `tests/test_audit.py:60-67`.
  - **Acceptance probe (run from the repository root):**
    ```sh
    python3 - <<'PY'
    import sys
    sys.path.insert(0, "src")
    from lean_parser import extract_axioms, extract_declaration_names

    text = "/-\naxiom ghost : True\n-/\nnamespace N\n  axiom real : True\n  theorem shown : True := by trivial\nend N"
    assert extract_axioms(text) == ["real"]
    names = extract_declaration_names(text)
    assert "real" in names
    assert "shown" in names
    assert "ghost" not in names
    PY
    python3 -m pytest tests/test_audit.py::test_no_project_axioms tests/test_audit.py::test_declaration_counts -q
    ```
  - **Dependencies/constraints:** Coordinate with MA-004 so both features share correct comment/string lexical handling. Preserve the frozen package's zero-project-axiom result and existing declaration count; changing that real-data count would require evidence in the package, not merely a parser preference.

- [ ] **MA-006 — P2 — Bind each audited quotation to its intended package file**
  - **Observable outcome:** A line-anchored quote passes only when its number and bytes match the designated source file; identical text at the same line in another package file can no longer rescue a bad citation. Existing valid quotations remain accepted.
  - **Evidence:** `scripts/check_quotations.py:21` discards paths after using basenames as dictionary keys, and `scripts/check_quotations.py:30-38` accepts a line-anchored quote when `any` source has matching text at that line. Bare quotes likewise use `any` at `scripts/check_quotations.py:39-42`. The Markdown filename is used only in failure reporting, not source selection. This is weaker than the repository's file-and-line citation doctrine at `AGENTS.md:5-7`.
  - **Acceptance probe (run from the repository root):** Add a temporary end-to-end fixture containing `A.lean` and `B.lean` and one finding whose quote is explicitly assigned to `A.lean`. Put the quoted bytes only at the cited line of `B.lean`, then invoke `python3 scripts/check_quotations.py "$tmp/docs" "$tmp/pkg"` and require exit status 1. Put the bytes at the cited line of `A.lean`, rerun the same CLI, and require status 0. Finally run `python3 scripts/check_quotations.py` against the real docs/package and require its reported failure count to remain zero.
  - **Dependencies/constraints:** First derive source association from existing finding structure where unambiguous; add explicit source metadata only where needed and migrate all current quotes atomically. Preserve support for both quote forms and the CLI's two optional directory arguments. Do not modify quoted package files to satisfy the gate.

- [ ] **MA-007 — P2 — Declare and document the test-runner dependency for a fresh environment**
  - **Observable outcome:** A contributor following one documented setup command obtains pytest without installing an undeclared global tool, then can run the complete suite; pytest remains a development-only dependency rather than a runtime dependency of the audit library.
  - **Evidence:** `pyproject.toml:1-6` declares no runtime dependencies, and its complete visible configuration at `pyproject.toml:8-10` only configures rather than declares pytest. Nevertheless `tests/test_audit.py:9` imports it and `tests/test_audit.py:25-37` uses its fixture decorator, while `README.md:30-34` goes directly to `python3 -m pytest` with no installation step.
  - **Acceptance probe (run from the repository root):** In a newly created virtual environment with only the project's documented bootstrap prerequisites, execute the new setup command exactly as written and then run `python3 -m pytest tests/ -q`; setup must provide pytest and all tests must pass. As the runtime-contract check, also run `python3 scripts/run_audit.py --output "$(mktemp)/audit.json"` in an environment without the development group and require success.
  - **Dependencies/constraints:** Choose pytest requirement/lock changes only after inspecting the actual resolver lock; do not invent an upgrade or add pytest to `[project].dependencies`. Preserve `requires-python = ">=3.11"` (`pyproject.toml:5`), the existing pytest configuration, and the Lean toolchain pin. No scientific/deployment constraint in the visible packet justifies changing the Python runtime floor.

- [ ] **MA-008 — P3 — Replace the no-op Navier-Stokes/BSD test loop with independent executable cases**
  - **Observable outcome:** Navier-Stokes and BSD each have a separately reported test case asserting `theorem_kind == "def"`; the self-comparing loop and unused loop variable disappear without weakening either assertion.
  - **Evidence:** At `tests/test_audit.py:101-103`, `v.problem == v.problem` is tautological, has no assertion, and the loop body does not use `prob`. The actual checks occur only afterward at `tests/test_audit.py:104-107`, so the loop contributes no validation and obscures the intended two-problem parameterization.
  - **Acceptance probe (run from the repository root):**
    ```sh
    python3 -m pytest tests/test_audit.py::test_ns_and_bsd_are_defs -q
    ```
    The collected node must expand to two independently named cases and both must pass. Then run the complete `python3 -m pytest tests/ -q` to account for the intentional collected-test-count change.
  - **Dependencies/constraints:** Use pytest's existing parameterization support; no new dependency is needed beyond MA-007. Keep the current module-scoped real-data verdict fixture and update the snapshot test-count wording at `README.md:9` and `README.md:27` if it changes.

- [ ] **MA-009 — P3 — Report logical file lines accurately when the final newline is absent**
  - **Observable outcome:** Inventory metadata reports one line for a nonempty unterminated file, `n + 1` lines for `n` newline characters with trailing content, and zero for an empty file, while byte counts and SHA-256 values remain unchanged.
  - **Evidence:** `src/evidence.py:31-39` sets `"lines": text.count("\n")`; this is a newline count, not a logical line count, and undercounts whenever the last line lacks a newline. That metadata is exposed as line counts by `scripts/run_audit.py:34-37` and serialized into the report at `scripts/run_audit.py:63-80`.
  - **Acceptance probe (run from the repository root):**
    ```sh
    python3 - <<'PY'
    import sys, tempfile
    from pathlib import Path
    sys.path.insert(0, "src")
    from evidence import EvidenceStore

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "sample.txt"
        path.write_bytes(b"first\nlast")
        item = EvidenceStore(tmp).inventory()["sample.txt"]
        assert item["lines"] == 2
        assert item["bytes"] == len(b"first\nlast")
        path.write_bytes(b"")
        assert EvidenceStore(tmp).inventory()["sample.txt"]["lines"] == 0
    PY
    python3 -m pytest tests/test_audit.py::test_package_files_present -q
    ```
  - **Dependencies/constraints:** Correct the derived metadata only; do not add newlines to or otherwise modify the frozen evidence files. Regenerate downstream report metadata through the separated-output path from MA-002 and review any resulting reported line diff rather than assuming every package file currently has a trailing newline.

### Review boundary

This is a source-only, bounded packet review. No command was executed during the review. The visible excerpts do not include the Lean proof files, generated JSON reports/data, manuscript/audit-document bodies, lockfile contents, or CI/deployment configuration beyond the supplied inventory; findings above therefore rely only on the cited visible lines. `package/MillenniumLean/audit.py` was inspected solely to understand the mirrored parser and remains frozen third-party evidence, not a production substitute to edit. No mock/fallback/fake/stub/`NotImplemented`/`pass`/TODO production substitution was found in the visible project code, and no dependency or toolchain upgrade is recommended without further evidence.
