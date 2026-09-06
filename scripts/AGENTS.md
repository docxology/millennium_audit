# scripts/ - Agent Notes

Thin-orchestrator contract: scripts in this directory do path bootstrap,
argument handling, logging/printing, and a single delegated call into
`../src/` entrypoints. No business/data/analysis logic here; anything
reusable belongs in `../src/` with tests in `../tests/`.

Inventory (complete for this directory):

- `run_audit.py` - full audit pipeline: inserts `../src/` on `sys.path`,
  delegates to `evidence`, `lean_parser`, `statement_audit`,
  `clay_statements`, `verdicts`; writes `../data/audit_report.json`.
- `check_quotations.py` - Layer 5 quotation gate
  (docs/approach/audit-doctrine.md): checks every `> N: text` and bare
  quote in `../docs/audit/*.md` byte-exact against
  `../package/MillenniumLean`; self-contained, no `src/` imports.

Gotchas:

- `run_audit.py` inserts `../src/` on `sys.path` by design (project-local
  import, no package installation).
- Both scripts take optional positional args, not flags (no `--help`);
  paths default relative to the script location, so they run from anywhere.
- `check_quotations.py` exit 1 means a doc quote no longer matches the
  extracted package bytes; reconcile the doc or the extraction, not the gate.
