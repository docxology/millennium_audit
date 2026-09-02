# MillenniumLean Audit — Findings Index

**Audited artifact:** `package/MillenniumLean/` (AIX Global, Inc.), from
Zenodo DOI 10.5281/zenodo.22226553, zip `MillenniumLean_ClayProof_20260901.zip`.
Audit session: 2026-09-01. All quotations are verbatim with `file:line` anchors
verified against the extracted tree; SHA-256 inventory in `../../data/audit_report.json`.

**Headline verdict: The package resolves none of the six Clay Millennium
Problems.** Its kernel-checked theorems are real (F01) but are not the Clay
statements: four finals carry the conjectures as unproved premise binders
(Riemann, Yang-Mills, P vs NP - F07, F04, F08) and two are definitions of
the open statements (F05, F06). Whether the problems are resolved in the
wider literature is outside this audit's evidence base. (The package does
contain genuine small theorems and faithful formalizations - itemized with
credit in F13.) The package's mathematical content is
carried by unproved premise binders, defs of open statements, and the trivial
tower invariant `0 < n + 1`.

| # | Finding | Verdict tag | One-line summary |
|---|---------|-------------|------------------|
| F01 | Kernel build & axiom footprints | CONFIRMED (pack) / VERIFIED (repro) | Their kernel claims are real — and evidentially void |
| F02 | Tower invariant `declInv n := 0 < n + 1` | REFUTES headline | The "universalization tower" proves `0 < n+1` |
| F03 | Hodge "final theorem" is list arithmetic | REFUTES coverage | `conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1]` by decide |
| F04 | Yang–Mills final is substitution | REFUTES headline | `0 < c → m = c → 0 < m` by `hid ▸ hc` |
| F05 | Navier–Stokes: def of the open problem | REFUTES headline | `ns_official` is a def; tower theorem is trivial |
| F06 | BSD: def of the open problem | REFUTES headline | `bsd_official` defines; nothing proves rank=ord |
| F07 | Riemann: conditional on the open problem | REFUTES headline | Premise `corr` IS the Hilbert–Pólya correspondence |
| F08 | P vs NP: conditional on unresolved premises | REFUTES headline | `hlb` + `bridge` restate the conjecture |
| F09 | audit.py "CLOSED" category error | CONFIRMED (misleading) | Def binder-closedness treated as proof-closedness |
| F10 | Axiom-footprint rhetoric | REFUTED (as argument) | "Premises would appear as axioms" is false |
| F11 | "Poincaré positive control" | SELF-DEFEATING | Control proves the same tautology as the six |
| F12 | Klein/ZMod-12 and theta-gap theorems | OFF_TOPIC (real but unrelated) | True finite arithmetic, no Clay content |
| F13 | Genuine real content in the package | CONFIRMED (fair credit) | Small true mathlib-anchored lemmas, itemized |
| F14 | External context: FTQC claim record | CONFIRMED (third-party) | Companion paper's claims publicly demolished |

Method note: every finding file pairs (a) the claim under audit, (b) verbatim
quotation(s), (c) a probe actually run this session, (d) fair analysis
including what is genuinely real, (e) a verdict tag
CONFIRMED / REFUTES-headline / PLAUSIBLE / [UNVERIFIED].

## Self-audit receipt

A verification pass (2026-09-01) parsed every line-anchored quotation in all
15 files and checked each against the extracted package bytes, line number
and text both: 259/259 quoted lines verify byte-exact against
package/MillenniumLean/. An earlier draft pass failed this check (51
transcription divergences in F07-F14); all quote blocks were rebuilt
programmatically from the package bytes and re-verified. The index and
findings were authored from verbatim in-session reads; the kernel facts in
F01 were independently reproduced (build exit 0, axiom report byte-identical
to the package's committed receipt - see ../../data/BUILD_RECEIPT.md).

## Audit fairness statement

- No kernel output of the package is disputed anywhere in this audit; all
  were independently reproduced and agree.
- Every "REFUTES HEADLINE" verdict cites the package's own source lines; the
  refutation is of the claimed demonstration, not of any kernel fact.
- F13 itemizes and credits every genuine result in the package.
- F14 is recorded as context only; removing it leaves the verdict unchanged.
- The one methodological soft spot, disclosed: mathlib was shallow-cloned at
  the exact pinned revision rather than full-history cloned; this affects
  provenance decoration only, not the kernel check.

## Red-team pass receipt (2026-09-01, pre-publication)

Three independent hostile-review lanes were dispatched against this audit
before publication:

1. **Statement-lane (F02-F08):** all seven findings re-verified byte-exactly
   against the package; all survive CONFIRMED. One precision note (F07's
   prose transliteration of the corr premise, already programmatically
   quote-anchored) and two minor items (ns_official/bsd_official appear in
   the package's own print_axioms.lean - now folded into F09 as
   reinforcement).
2. **Meta-lane (F09-F11 + headline):** the audit is fair to the package's
   audit.py (F09, if anything, understates the README prose overclaim); F10
   correctly grants the narrow true claim before refuting the wide one; F11
   and the headline verdicts hold.
3. **Process-lane:** orchestrator re-run reproduces data/audit_report.json
   exactly; 15/15 tests pass; independent quotation re-check 257/267 with
   the 10 flagged lines all resolved as checker-side source-file
   misattributions (verified byte-exact against README.md:121-124); doctrine
   verification-chain layers each map to a real artifact.

Rating: process integrity SOLID. Corrections applied from the pass (all
probe-verified against package bytes before editing): F04 precision note
(hc is dischargeable via ym_center_flux_pos:119; the load-bearing premise
is hid); F06 strengthened (the _hL premise is underscore-named and never
used - L is a free function despite the docstring claim); F07 annotated
(riemann_official:52 is a proof-free def alias with no consuming theorem);
F09 reinforced via print_axioms.lean. Post-correction gate: 259/259 quotes
byte-exact, 15/15 tests pass.


## Meta-lane and process-lane receipts (2026-09-01, full reports)

**Meta-lane (F09-F11 + headline):** F09 fair and, if anything, understates
the package's overclaim (README.md:110 asserts a negative existential about
unproved premises a name-based parser cannot establish; README.md:147
asserts premises are "committed spectral certificates" when no such terms
ship in the zip). F10 confirmed fair and self-consistent. F11 verdict
survives with one clause softened (the tautological control does carry
build/toolchain smoke-test information - now reflected in F11). F14
quarantine verified non-load-bearing by grep. Headline reworded from a
world-claim to a package-attributed claim (above), provable from in-package
evidence alone.

**Process-lane:** orchestrator re-run reproduces data/audit_report.json
exactly; independent quotation re-verification 267/267 byte-exact (all 10
flagged lines hand-confirmed against README.md:121-124 and :158-163);
15/15 tests pass; every manuscript number recomputes; all doctrine
verification-chain layers map to real artifacts. Rating: MINOR-GAPS, with
all three gaps fixed in this pass: (a) quotation-gate script now committed
as scripts/check_quotations.py (re-runnable); (b) "11 files" corrected to
"10 files plus one directory entry" in F14 and the manuscript; (c) the
no-version-control caveat is disclosed here - Millennium_Audit is a
working-tree project; the regenerated audit_report.json relies on the
in-session receipt and the package SHA-256 pins rather than a git baseline.

Post-correction gate: 259/259 quotes byte-exact (re-run via the committed
script), 15/15 tests pass.