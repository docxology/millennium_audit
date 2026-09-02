# docs/ - Agent Notes

- The findings under `audit/` are evidence artifacts: every quotation is
  line-anchored and was script-verified (259/259 byte-exact) against
  `package/MillenniumLean/`. If you edit a finding, re-run the quotation
  check; if you quote the package in new prose, add the quote to the check.
- The manuscript under `manuscript/` follows the template manuscript
  contract: numbers must be supported by `../data/audit_facts.json` (the
  evidence registry validates this in stage 04). After any manuscript edit,
  re-run stage 03 (render) and stage 04 (validate) from the repo root.
- Do not modify `package/MillenniumLean/` - it is the verbatim evidence
  under audit.
