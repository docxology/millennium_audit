# Audit tests

Run the audit tests from the repository root with uv. The project supports
Python 3.11 or newer and selects Python 3.15 by default.

```sh
uv sync --locked
uv run --locked pytest tests/
```

[`test_audit.py`](test_audit.py) checks the tracked MillenniumLean working
copy, statement classifications and the [recorded report](../data/audit_report.json).
It also checks that an alternate source audit writes a separate report and that
the quotation checker verifies the published ZIP.

For the individual source and quotation commands, see the
[reproduction guide](../docs/reproduce.md) and
[command reference](../docs/reference/commands.md). The
[Lean build receipt](../data/BUILD_RECEIPT.md) records the separate kernel run
against the original archive.
