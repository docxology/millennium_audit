# scripts/ - Agent Notes

Thin-orchestrator contract: scripts in this directory do path bootstrap,
argument handling, logging/printing, and a single delegated call into
`../src/` entrypoints. No business/data/analysis logic here; anything
reusable belongs in `../src/` with tests in `../tests/`.

## Audit commands

Run from the repository root. See the [command reference](../docs/reference/commands.md)
for the supported arguments.

- `run_audit.py` audits the tracked `package/MillenniumLean/` by default.
  It accepts an optional package path and `--output`. Use
  `uv run --locked python scripts/run_audit.py --output output/current-audit-report.json`
  for a fresh report alongside the committed reference. With the tracked package
  and no output argument, it writes `data/audit_report.json`. The runner uses
  `output/alternate-audit-report.json` for alternate inputs without a supplied
  output path and rejects the recorded destination for those inputs.
- `check_quotations.py` checks numbered source lines and eligible bare excerpts
  in `docs/audit/` against `MillenniumLean_ClayProof_20260901.zip` by default.
  It accepts an optional positional findings directory followed by a source ZIP
  or directory. Exit 1 reports quotation mismatches.

The source runner imports the local `src/` modules. The quotation checker
reads the selected source directly. See the [test guide](../tests/README.md)
for the locked test command.
