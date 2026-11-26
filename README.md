# Millennium_Audit

Forensic audit of the MillenniumLean package (AIX Global, Zenodo
[10.5281/zenodo.22226553](https://doi.org/10.5281/zenodo.22226553)) — a Lean 4
package claiming kernel-checked proofs of the six remaining Clay Millennium
Problems.

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22243473-blue)](https://doi.org/10.5281/zenodo.22243473)

[Documentation](docs/README.md) · [Reproduce the audit](docs/reproduce.md) · [Manuscript source](docs/manuscript/README.md)

**Verdict: the package resolves none of the six problems.** The published
[build receipt](data/BUILD_RECEIPT.md) records a clean build, zero live `sorry`
and zero project axioms for the reviewed archive. The theorem types
are conditional implications carrying the open problems as unproved premises
(Riemann, Yang-Mills, P vs NP), definitions of the open statements
(Navier-Stokes, BSD), or true theorems about unrelated objects (Hodge: a list
identity). The universalization tower proves only `0 < n + 1`.

## Repository layout

| Path | Contents |
|------|----------|
| `docs/audit/` | 22 itemized findings (F01-F22), each quote-anchored to the package |
| `docs/approach/` | Audit doctrine and method |
| `docs/manuscript/` | Maintained research manuscript |
| `MillenniumLean_ClayProof_20260901.zip` | Published package bytes used by the quotation check |
| `package/MillenniumLean/` | Tracked working copy for the source-audit runner and its tests |
| `src/`, `scripts/`, `tests/` | Audit logic, orchestrator and real-data tests |
| `data/` | Build receipt, statement evidence, machine-readable reports |

## Run the audit

```sh
uv sync --locked
uv run --locked python scripts/run_audit.py --output output/current-audit-report.json
uv run --locked python scripts/check_quotations.py
uv run --locked pytest
```

## Publication

- **DOI:** [10.5281/zenodo.22243473](https://doi.org/10.5281/zenodo.22243473)
  (concept: 10.5281/zenodo.22243472) — rendered PDF + complete evidence bundle
- **docxology site entry:** [danielarifriedman.com/papers/2026_MillenniumAudit](https://danielarifriedman.com/papers/2026_MillenniumAudit/)
- Audited package: [10.5281/zenodo.22226553](https://doi.org/10.5281/zenodo.22226553)
- Citation: see [docs/publication.md](docs/publication.md) · [CITATION.cff](CITATION.cff)

The [reproduction guide](docs/reproduce.md) covers source selection, the
Lean build receipt and clean Template rendering.
