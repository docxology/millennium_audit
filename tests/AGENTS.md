# tests/ - Agent Notes

- No mocks: every test reads `../package/MillenniumLean/` bytes (the
  template's zero-mock policy).
- Tests are part of the verification chain: each encodes a finding's
  load-bearing claim. If a test fails after a package change, that is a
  FINDING-LEVEL event, not a test to update reflexively - investigate first.
- Run one pytest invocation for this project only (template conftest-collision
  rule).
