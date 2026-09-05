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
tower invariant `0 < n + 1`. A rebuttal-response pass (2026-09-04, F15-F22) re-verified the
audit against the md5-pinned Zenodo deposit after the authors' LinkedIn rebuttal: the paper's
Section-4 `*_final` theorems and `gftqc_*` certificates do not exist in the published,
kernel-checkable package; the headline verdict is unchanged.

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
| F15 | Rebuttal pass: the six `*_final` theorems | REFUTES HEADLINE | Paper §4's closed finals exist only as prose; package census has none |
| F16 | Paper §4 Lean block vs package types | REFUTES HEADLINE | Block needs 22 undeclared identifiers; Hodge/NS/ YM consumption impossible as typed |
| F17 | "Named consumed certificates" are axioms | REFUTES HEADLINE | Kernel receipt: consumed certificates print in `#print axioms` (F17 probe) |
| F18 | ComplexityModel junk instantiation | REFUTES HEADLINE | Junk model yields closed zero-axiom P≠NP |
| F19 | `Promote.tower_closes` proves any declared target | CONFIRMED (content-free) | Junk-tower receipt; the "corrected" mechanism is plumbing too |
| F20 | Division of labor: certificates must ship | REFUTES HEADLINE | Architecture conceded; the verifiable layer ships zero certificate terms |
| F21 | `gftqc_corr` ≡ the Hilbert–Pólya binder | REFUTES HEADLINE | Paper's 7.1 is the package's unproved `corr` premise (F07); no term ships |
| F22 | Rebuttal census + requirements on a responsive deposit | REFUTES HEADLINE (as of pinned md5) | Per-problem absence table + kernel-falsifiable checklist |
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

## Rebuttal-pass receipt (2026-09-04, F15-F22)

Trigger: the authors' LinkedIn rebuttal (D. Ovseyenko, 2026-09-04) states the audit attributed the
proofs to the generic tower machinery, and points to the paper's Section-4 closed finals
(`riemann_final` … `p_neq_np_final`) consuming named `gftqc_*` certificates.

Probes run this session (all in-session, receipts inside the finding files):

- **Artifact identity:** audited zip md5 `99df5b03a4798bfe543b03f525face13` equals the file md5
  listed on the live Zenodo record 22226553 (v2, published 2026-09-01) — the audited artifact is
  the currently published one; all compared zip members byte-identical to `package/MillenniumLean/`
  (SHA-256, 7 files).
- **Identifier census:** `gftqc`, `_final`, `StandardComplexityModel` — 0 occurrences in the
  package (all .lean and .md); full declaration census 41 declarations, none named `*_final`/
  `gftqc_*`; the only `Official*` is the field `OfficialTarget` (Millennium.lean:360).
- **Lean probes (lake env lean, Lean 4.34.0-rc1, pinned mathlib, exit 0):** (1) junk
  ComplexityModel yields a closed zero-axiom `P_neq_NP` (F18); (2) named certificates consumed by
  a closed final print as axioms — `[gftqc_bridge, gftqc_hlb, propext, Classical.choice,
  Quot.sound]` (F17); (3) a junk `PromotableTower` closes any declared target via
  `Promote.tower_closes` (F19).
- **Mathlib census at pinned revision:** zero `Chow` files; no Hodge-conjecture statement object
  (only incidental p-adic Hodge–Tate mentions) — F16.
- **Paper text:** v1.0 PDF (md5 6005a74c3db1d3d729263996e395f6e3, matching the live record)
  fetched and text-extracted; §4 block and §7.1/§10/§11 quotations in F15/F16/F21 are from the
  published PDF text.

Scope discipline preserved: no kernel output of the package is disputed; the quantum-layer claims
remain quarantined as context (F14 policy); the audit is strictly Lean-artifact-level, per the
audit scope. The paper's Section-4 block is quoted from PDF text extraction (ligatures normalized);
the package census and Lean probes are byte/exit-0 receipts.

## Red-team refute-pass receipt (2026-09-04/05, F15-F22)

Five adversarial lanes (scout workers, no edit rights) were dispatched to REFUTE the new findings;
each re-ran its assigned checks independently. Result: **F15-F22 all SURVIVE**, zero findings
refuted, no kernel facts disputed, no overstatement found. Receipts:

- refute#1 (F15): md5 identity re-verified via Zenodo API (v2 = 22226553, md5 99df5b03…, 22141 B;
  concept's earlier version = record 22225697, md5 c20731d652568a954afe1c66b45df1b3, 21450 B);
  grep census 0 hits; 41 declarations; endpoint table vs README:7-14 and print_axioms.lean:8-13 —
  all reproduced. Stronger than claimed: ALL TEN zip members SHA-256-identical (finding said
  seven compared). Applied.
- refute#2 (F16): PDF quotations verbatim; Fraisse.lean hit identified as the surname "Hodges"
  (strengthens the mathlib-absence point) — applied; ComplexityModel/P_neq_NP-exist note applied.
- refute#3 (F17): Lean probe re-run, exit 0, footprint byte-identical; named-certificate
  dichotomy confirmed exhaustive; anonymous-inline-term caveat added to the finding.
- refute#4 (F18, F19): full lake build (8729 jobs) + probe re-run, exit 0, outputs byte-identical;
  no overstatement (neither claims impossibility of a faithful instance — only its absence from
  the deposit).
- refute#5 (F20/F21/F22): README:147-149 byte-faithful; census table row-by-row confirmed;
  F22 falsifiability claim softened (items 1-3 kernel-checkable; 4-5 by inspection/build) —
  applied; gftqc_hodge_algebraic/gftqc_hodge dual-naming and hL/_hL nits recorded in F22.

Post-refute gate: 292/292 quotes byte-exact, 15/15 tests pass, orchestrator re-run reproduces
data/audit_report.json identically.