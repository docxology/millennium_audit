# Epistemic Status

Validated in this audit session (2026-09-01), all by direct execution or
verbatim read:

- All 10 package files read (11 unzip entries incl. directory); SHA-256 inventory recorded (data/audit_report.json).
- Kernel reproduction completed: pinned toolchain v4.34.0-rc1 installed;
  mathlib at pinned revision d0be1efe9afff6119115373bf4ea5abd833b3a95;
  `lake build Tower Millennium` exit 0 ("Build completed successfully
  (8730 jobs)"); `lake env lean print_axioms.lean` exit 0 with the six
  footprint lines byte-identical to the package's committed receipt
  (data/BUILD_RECEIPT.md).
- The package's own audit.py executed unmodified; its committed output
  reproduced.
- Independent binder parsing of all six finals (src/lean_parser.py);
  verdicts recorded in data/audit_report.json.
- 15/15 tests pass against the real package bytes (no mocks).
- 259/259 line-anchored quotations across docs/audit/*.md verified
  character-exact against the extracted sources; an earlier draft failed
  this check and was rebuilt programmatically (disclosed in 00_INDEX.md).

Unverified / disclosed limits:

- mathlib was shallow-cloned at the exact pinned revision (provenance
  decoration only; the kernel checks the checked-out tree).
- Third-party web claims (F14) are recorded as reported by their sources,
  not independently investigated.
- Classification of edge cases (conditional vs off-topic) involves judgment;
  every classification here is over-determined by multiple quotes.

Nothing in the verdict depends on any unverified item.
