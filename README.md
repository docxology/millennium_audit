# Millennium_Audit

Forensic audit of the MillenniumLean package (AIX Global, Zenodo
[10.5281/zenodo.22226553](https://doi.org/10.5281/zenodo.22226553)) — a Lean 4
package claiming kernel-checked proofs of the six remaining Clay Millennium
Problems.

[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.22243473-blue)](https://doi.org/10.5281/zenodo.22243473)
[![Tests](https://img.shields.io/badge/tests-15%2F15-brightgreen)]()

**Verdict: the package resolves none of the six problems.** Its kernel claims
are true and independently reproduced (clean build, zero `sorry`, zero project
axioms under the pinned toolchain) — and evidentially void: the theorem types
are conditional implications carrying the open problems as unproved premises
(Riemann, Yang-Mills, P vs NP), definitions of the open statements
(Navier-Stokes, BSD), or true theorems about unrelated objects (Hodge: a list
identity). The universalization tower proves only `0 < n + 1`.

## Repository layout

| Path | Contents |
|------|----------|
| `docs/audit/` | 14 itemized findings (F01-F14), each quote-anchored to the package |
| `docs/approach/` | Audit doctrine and method |
| `docs/manuscript/` | Research manuscript (rendered: `output/pdf/`) |
| `package/MillenniumLean/` | The audited artifact, verbatim (evidence; do not modify) |
| `src/`, `scripts/`, `tests/` | Audit logic, orchestrator, 15 real-data tests |
| `data/` | Build receipt, statement evidence, machine-readable reports |

## Run the audit

    python3 scripts/run_audit.py           # report + data/audit_report.json
    python3 scripts/check_quotations.py    # 259/259 byte-exact quotation gate
    python3 -m pytest tests/ -q            # 15 tests, no mocks

## Publication

- **DOI:** [10.5281/zenodo.22243473](https://doi.org/10.5281/zenodo.22243473)
  (concept: 10.5281/zenodo.22243472) — rendered PDF + complete evidence bundle
- **docxology site entry:** [danielarifriedman.com/papers/2026_MillenniumAudit](https://danielarifriedman.com/papers/2026_MillenniumAudit/)
- Audited package: [10.5281/zenodo.22226553](https://doi.org/10.5281/zenodo.22226553)
- Citation: see [docs/publication.md](docs/publication.md) · [CITATION.cff](CITATION.cff)

See [STANDALONE.md](STANDALONE.md) for what a separated copy must still
explain.
