# Methodology

## Artifacts

The audited artifact is the Zenodo zip MillenniumLean_ClayProof_20260901.zip
(10 files plus one directory entry, 50,708 bytes), extracted unmodified to
package/MillenniumLean/ with a SHA-256 inventory recorded in
data/audit_report.json. The zip was neither edited nor re-packed; all
quotations anchor to this extracted tree.

## Kernel reproduction (independent)

- Toolchain: elan installed leanprover/lean4:v4.34.0-rc1 exactly as pinned in
  lean-toolchain.
- mathlib: shallow-cloned at the revision pinned in lake-manifest.json
  (d0be1efe9afff6119115373bf4ea5abd833b3a95); HEAD verified on the checkout;
  prebuilt oleans restored via `lake exe cache get` (8,711 files).
- Build: `lake build Tower Millennium` in a clean workspace containing the
  package's six source/config files verbatim -> "Build completed successfully
  (8730 jobs)", exit 0.
- Axioms: `lake env lean print_axioms.lean` -> exit 0; the six footprint lines
  match the package's PROOF_CERTIFICATE.md verbatim.
- Receipt: data/BUILD_RECEIPT.md.

One disclosed soft spot: mathlib was shallow-cloned at the exact pinned
revision rather than full-history cloned. This affects provenance decoration
only, not the kernel check (the kernel checks the checked-out tree's oleans).

## Statement-level audit

Each claimed "final theorem" was parsed from Millennium.lean by a
balanced-parenthesis binder extractor (src/lean_parser.py) that records the
declaration kind (theorem vs def) and every explicit premise binder - the
same mechanics as the package's own audit.py, re-implemented and tested. Each
final was then compared against the official Clay statement (the oracle in
src/clay_statements.py, from the Clay problem PDFs) and classified:

- CONDITIONAL_IMPLICATION - the type carries unproved premise binders;
- DEFINITION_ONLY - a def of the open statement;
- OFF_TOPIC_THEOREM - closed type, but no Clay object in it.

The package's own audit.py was also executed unmodified; its committed output
reproduces.

## Verification of the audit itself

All fifteen test files in tests/ assert audit facts against the real package
bytes (no mocks; 15/15 pass). All 259 line-anchored quotations in
docs/audit/*.md were script-checked against the extracted sources - line
number and text both - with zero divergence. An earlier draft failed this
check (51 divergences from Unicode normalization); all quote blocks were
rebuilt programmatically from the package bytes and re-verified. The
failure-and-fix is disclosed in docs/audit/00_INDEX.md.

## Line-by-line verification of the package (whole-file)

- Millennium.lean (404 lines): read verbatim; 35 declarations.
- Tower.lean (30 lines): read verbatim; 6 declarations + 3 #print commands.
- audit.py (69 lines): executed; parsing logic reviewed line-by-line.
- PROOF_CERTIFICATE.md (105 lines), WHY_THIS_IS_PROOF.md (70 lines),
  README.md (167 lines): read verbatim; every checkable claim traced to a
  declaration or marked unverified.
- lakefile.toml, lake-manifest.json, lean-toolchain, print_axioms.lean:
  inspected; manifest revision cross-checked against the clone.
