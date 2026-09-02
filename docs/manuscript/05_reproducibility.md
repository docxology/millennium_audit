# Reproducibility of this audit

Everything re-runs from the repository root:

    python3 projects/working/Millennium_Audit/scripts/run_audit.py
    # -> console report + data/audit_report.json (machine-readable)

    uv run pytest projects/working/Millennium_Audit/tests/
    # -> 15 real-data tests against the extracted package

    .venv/bin/python -m pytest tests/ -q          # from the project dir

Lean reproduction (receipt: data/BUILD_RECEIPT.md):

    elan toolchain install leanprover/lean4:v4.34.0-rc1
    # mathlib at pinned rev d0be1efe9afff6119115373bf4ea5abd833b3a95
    lake exe cache get
    lake build Tower Millennium
    lake env lean print_axioms.lean

Findings: one file each under docs/audit/F01-F14, indexed by docs/audit/
00_INDEX.md, which also records the 259/259 quotation-verification receipt.

## Published record

DOI: 10.5281/zenodo.22243473 (concept DOI 10.5281/zenodo.22243472). The
Zenodo deposit contains this manuscript's rendered PDF, all fourteen finding
files, the audit doctrine, the build receipt, the statement-evidence
analysis, and both machine-readable reports. The docxology paper folder
(github.com/docxology/docxology, papers/2026_MillenniumAudit) mirrors the
rendered PDF and full text publicly.
