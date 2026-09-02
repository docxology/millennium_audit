# Millennium_Audit standalone guide

Millennium_Audit is its own repository — `docxology/millennium_audit` — as well
as a working project inside the template tree it was developed in. The audit
logic (`src/`), the thin orchestrator (`scripts/run_audit.py`), the real-data
test suite (`tests/`, 15 tests), and the verbatim evidence tree
(`package/MillenniumLean/`) all run from the clone alone.

## What a separated copy must still explain

**What it is.** A forensic audit of one artifact: the MillenniumLean package
(AIX Global, Zenodo 10.5281/zenodo.22226553) claiming kernel-checked Lean 4
proofs of the six remaining Clay Millennium Problems.

**Its verdict.** The package resolves none of the six problems: its kernel
claims are true and independently reproduced (findings F01), and its theorem
types are conditionals, definitions, or list arithmetic (F02-F08). The
universalization tower proves only `0 < n + 1` (F02).

**How to re-run the audit.**

    python3 scripts/run_audit.py           # report + data/audit_report.json
    python3 scripts/check_quotations.py    # 259/259 byte-exact quotation gate
    .venv/bin/python -m pytest tests/ -q   # 15 tests, no mocks

The Lean kernel reproduction requires the pinned toolchain
(leanprover/lean4:v4.34.0-rc1) and mathlib at manifest revision d0be1efe9a;
see data/BUILD_RECEIPT.md for the completed receipt.

**Publication.** Zenodo DOI 10.5281/zenodo.22243473 carries the rendered PDF
and the complete evidence bundle. `CITATION.cff` and `.zenodo.json` carry the
same metadata in machine-readable form.
