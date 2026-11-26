# Audit commands

Thin orchestrators: path bootstrap, argument handling, and printing only.
See the [source index](source.md) and [verification guide](tests.md).

| script | purpose | delegates to | run command |
|--------|---------|--------------|-------------|
| `run_audit.py` | SHA-256 inventory, source hygiene checks and statement verdicts | `src/evidence.py`, `src/lean_parser.py`, `src/statement_audit.py` and report data | `uv run --locked python scripts/run_audit.py --output output/current-audit-report.json` |
| `check_quotations.py` | Match numbered and bare quotes against the published ZIP. Exit 1 on a mismatch. | Standalone checker | `uv run --locked python scripts/check_quotations.py` |

Pass the optional findings directory and source ZIP or directory to check a
different quotation set. Use a positional package path and `--output` to
produce a separate audit report.
