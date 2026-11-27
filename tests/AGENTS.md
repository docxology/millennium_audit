# tests/ - Agent Notes

- Start with the [test guide](README.md) for the locked command and audit inputs.
- Follow the zero-mock policy with real inputs from the tracked working copy,
  committed audit report and original publication archive.
- Tests are part of the verification chain: each encodes a finding's
  load-bearing claim. If a test fails after a package change, that is a
  FINDING-LEVEL event, not a test to update reflexively - investigate first.
- Run one pytest invocation for this project only (template conftest-collision
  rule).
