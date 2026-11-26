# Reproducibility of this audit

Run the source audit, archival quotation check and native tests from the
repository root. The report goes to a local output file.

```sh
uv sync --locked
uv run --locked python scripts/run_audit.py --output output/current-audit-report.json
uv run --locked python scripts/check_quotations.py
uv run --locked pytest
```

The historical Lean build and axiom-footprint receipt is recorded in
`data/BUILD_RECEIPT.md` for the original archive and its pinned dependencies.
The current working package has its own toolchain metadata. The repository
reproduction guide documents both source verification and the pinned
manuscript build.

Findings: one file each under docs/audit/F01-F22, indexed by docs/audit/
00_INDEX.md, which also records the quotation-verification receipts (259/259
original pass; 292/292 including the 2026-09-04 rebuttal pass) and the
red-team refute-pass receipt.

## Published record

DOI: 10.5281/zenodo.22243473 (concept DOI 10.5281/zenodo.22243472). The
Zenodo deposit contains this manuscript's rendered PDF, all twenty-two finding
files, the audit doctrine, the build receipt, the statement-evidence
analysis, and both machine-readable reports. The docxology paper folder
(github.com/docxology/docxology, papers/2026_MillenniumAudit) mirrors the
rendered PDF and full text publicly.
