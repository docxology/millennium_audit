# data/ - Agent Notes

- `audit_report.json` and `audit_facts.json` are GENERATED (by
  `scripts/run_audit.py` and the session measurements) - regenerate, do not
  hand-edit values to match prose. The template evidence registry validates
  manuscript numbers against `audit_facts.json`; add new measured facts there
  when new numbers enter the manuscript.
- `BUILD_RECEIPT.md` records a completed kernel reproduction; if you re-run
  the build under a different mathlib state, append a new receipt section
  rather than editing the existing one.
- `audit_facts.json.lean_source_line_anchors` pins the quoted line numbers;
  if the package under audit ever changes (it should not - it is evidence),
  re-verify all anchors before updating.
