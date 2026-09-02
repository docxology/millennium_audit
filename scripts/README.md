# scripts/

Thin orchestrators.

- `run_audit.py` - full audit: SHA-256 inventory, kernel-hygiene grep,
  statement verdicts, headline + epistemic records; writes
  `../data/audit_report.json`.

Run from anywhere: `python3 scripts/run_audit.py [path/to/MillenniumLean]`.
