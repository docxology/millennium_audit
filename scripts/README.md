# scripts/

Thin orchestrators: path bootstrap, argument handling, and printing only.
Logic lives in `../src/` (tested in `../tests/`).

| script | purpose | delegates to | run command |
|--------|---------|--------------|-------------|
| `run_audit.py` | Full audit: SHA-256 inventory, kernel-hygiene grep, statement verdicts, headline + epistemic records; writes `../data/audit_report.json` | `src/evidence.py`, `src/lean_parser.py`, `src/statement_audit.py`, `src/clay_statements.py`, `src/verdicts.py` | `python3 scripts/run_audit.py [path/to/MillenniumLean]` |
| `check_quotations.py` | Quotation gate (Layer 5): verifies every line-anchored and bare quote in `../docs/audit/*.md` byte-exact against `../package/MillenniumLean`; exit 1 on mismatch | self-contained (no `src/` module) | `python3 scripts/check_quotations.py [docs/audit] [package/MillenniumLean]` |
