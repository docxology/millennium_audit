# Audit Doctrine and Method

How the Millennium_Audit was designed and conducted. Findings live in
../audit/; this file records the approach.

## 1. Governing doctrine

Three principles, in priority order:

1. **Green is not proof.** A passing build, clean gate, or axiom-free
   footprint is a conjecture about what a claim demonstrates until an
   independent pass re-derives it. We reproduced every kernel claim before
   attacking any of them (finding F01), and we dispute none of them.
2. **Attack the type, not the kernel.** A Lean theorem is a proof of its
   TYPE. The decisive question for a "Millennium proof" claim is never
   "does it compile" but "what does the type say". All load-bearing
   analysis (F02-F08) is statement-level: binder parsing, declaration kind
   (theorem vs def), and comparison against the official Clay statements.
3. **Fairness is structural, not rhetorical.** Genuine content gets its own
   finding (F13) with every real result itemized; the external record (F14)
   is quarantined as context-only so the verdict stands without it; every
   refutation cites the package's own source lines.

## 2. Audit design

Four lenses, executed in order:

| Lens | Question | Instrument |
|------|----------|------------|
| Reproduction | Do the kernel claims reproduce? | Pinned toolchain + pinned mathlib build + axiom print (F01) |
| Statement | What does each final theorem's type actually say? | Binder parser + Clay-statement oracle (F02-F08) |
| Meta-audit | Is the package's own evidence honest? | Execute their audit.py; check its logic (F09, F10, F11) |
| Context | What does the public record show? | Web retrieval, quarantined to F14 |

## 3. Verification chain (what makes findings trustworthy)

Every layer of the audit is itself gated:

1. **Artifact integrity.** The Zenodo zip extracted unmodified; SHA-256 of
   all 11 files in data/audit_report.json.
2. **Kernel reproduction.** Toolchain installed from the package's own pin;
   mathlib checked out at the exact manifest revision; build exit 0; axiom
   report byte-identical to the package's committed receipt
   (data/BUILD_RECEIPT.md).
3. **Parser validation.** src/lean_parser.py re-implements the package's
   audit.py mechanics; both agree on binder lists; the package's audit.py
   was executed unmodified and reproduced its committed output.
4. **Test gate.** 15 real-data tests (tests/test_audit.py) assert the audit
   facts against package bytes - no mocks. Run: `.venv/bin/python -m pytest
   tests/ -q`.
5. **Quotation gate.** `scripts/check_quotations.py` parses every
   line-anchored quotation in docs/audit/*.md and verifies text and line
   number against the extracted sources: 259/259 byte-exact. The first
   draft failed (51 divergences from Unicode normalization in F07-F14);
   quote blocks were rebuilt programmatically from the package and
   re-verified to zero. Disclosed in the audit index. The script is
   committed and re-runnable (process-lane red-team gap, fixed 2026-09-01).
6. **Self-audit of verdicts.** Each verdict tag requires a probe actually
   run this session; PLAUSIBLE/[UNVERIFIED] tags were available and none of
   the load-bearing verdicts needed them.

## 4. Classification scheme

Each claimed final theorem is classified by what its TYPE does relative to
the official Clay statement:

- **CONDITIONAL_IMPLICATION** - type carries unproved premise binders
  (Riemann: hD, corr; Yang-Mills: hc, hid; P vs NP: hq, hlb, bridge).
- **DEFINITION_ONLY** - a def of the open statement (ns_official,
  bsd_official). A def proves nothing; binder-closedness of a def is
  meaningless (the package's own audit calls these "CLOSED" - the F09
  category error).
- **OFF_TOPIC_THEOREM** - closed type, but no Clay object in it
  (hodge_kunneth: list arithmetic).

Two cross-checks discipline the scheme: (a) the package's own audit.py
concedes CONDITIONAL for the same four finals; (b) every classification is
over-determined by multiple quotes (e.g. Yang-Mills is both conditional AND
its type is bare substitution).

## 5. The smoking gun, stated precisely

Tower.lean:11: `def declInv (n : Nat) : Prop := 0 < n + 1`. The theorems
named hodge, bsd, navier_stokes, poincare_control and five Tower wrappers
all equal Tower.universal over this invariant, proved from Nat.succ_pos.
Substituting the definition, each proves `forall n : N, 0 < n + 1`. The
package's own comment (Millennium.lean:337-341) claims this trivial invariant
was replaced with "mathematical content"; the replacement (Promote) is
generic plumbing whose tower_closes proves whatever a tower declares - and
the named theorems still consume the unchanged Tower.declInv.

## 6. Tooling map

| Path | Role |
|------|------|
| src/lean_parser.py | Binder extraction, declaration kinds, sorry/axiom grep (comment-aware) |
| src/clay_statements.py | Official Clay statements as comparison oracle |
| src/statement_audit.py | Classification engine (three verdict classes) |
| src/verdicts.py | Headline/tower/epistemic verdict records |
| src/evidence.py | SHA-256 inventory of the package |
| scripts/run_audit.py | Thin orchestrator -> data/audit_report.json |
| tests/test_audit.py | 15 real-data assertions |
| data/BUILD_RECEIPT.md | Lean reproduction receipt |
| data/STATEMENT_EVIDENCE.md | Per-problem file:line gap analysis |

## 7. Deliberate limits

- The package under audit is never modified; quotes anchor to the extracted
  tree's exact bytes.
- The proprietary quantum layer is not evaluated (the package itself says it
  is unnecessary for verification - true, and central to the problem: there
  is nothing substantive to verify).
- Third-party web claims are recorded as reported, quarantined to F14, and
  are not load-bearing for the verdict.
