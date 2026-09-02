# audit/ - Agent Notes

Editing discipline for findings:

1. Each finding must keep its five-part structure: claim under audit,
   verbatim quotation (line-anchored), probe actually run, fair analysis
   (including genuine content), verdict tag.
2. Quotations are checked byte-exact against `../../package/MillenniumLean/`
   (line number and text). Rebuild quote blocks programmatically from the
   package bytes; never retype Lean Unicode from memory.
3. Verdict tags: CONFIRMED / REFUTES HEADLINE / REFUTED / SELF-DEFEATING /
   OFF_TOPIC / [UNVERIFIED]. A tag requires a probe run in-session.
4. Fairness: F13 (genuine content) and the F14 quarantine (context-only,
   not load-bearing) are structural commitments of this audit - preserve
   them. No kernel output of the package is disputed anywhere.
