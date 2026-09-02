# src/ - Agent Notes

- Pure logic + explicit file I/O; no `infrastructure.*` imports (Layer-2
  project-local isolation).
- `lean_parser.py` must stay semantically aligned with the package's own
  `audit.py` binder mechanics (the meta-audit compares both); any parser
  change needs a matching test.
- All tests execute against real package bytes - no mocks (see
  `../tests/AGENTS.md`).
