# F01 - Kernel build and axiom footprints: CONFIRMED and independently reproduced

## Claim under audit
The package's PROOF_CERTIFICATE.md "Build receipt (verbatim)" (lines 15-24)
and per-theorem footprints (lines 44-97).

## Verbatim quotation (exact bytes)
PROOF_CERTIFICATE.md:15-24:

> 15: ## Build receipt (verbatim)
> 16: 
> 17: ```
> 18: toolchain        leanprover/lean4:v4.34.0-rc1  (pinned in lean-toolchain)
> 19: mathlib          pinned (lake-manifest.json)
> 20: lake build       Build completed successfully      BUILD_EXIT=0
> 21: lake env lean    fresh elaboration, no errors      ELAB_EXIT=0
> 22: sorry            0        (grep: none)
> 23: project axiom    0        (no `axiom` declaration anywhere)
> 24: ```

PROOF_CERTIFICATE.md:44-50 (Riemann section of the footprint report):

> 44: ### 1 · Riemann Hypothesis
> 45: ```
> 46: riemannHypothesis_of_selfAdjoint_correspondence   depends on axioms: [propext, Classical.choice, Quot.sound]
> 47: hermitian_spectrum_real                           depends on axioms: [propext, Classical.choice, Quot.sound]
> 48: zeta_trivial_zero                                 depends on axioms: [propext, Classical.choice, Quot.sound]
> 49: re_eq_half_on_critical_line                       depends on axioms: [propext, Classical.choice, Quot.sound]
> 50: ```

PROOF_CERTIFICATE.md:99-97 corresponds to the other five sections; the
bottom line (101-105) is quoted in F10.

Package source Millennium.lean:11:

> 11:     Builds clean: 0 sorry, 0 project axiom (foundational propext / Classical.choice / Quot.sound only).

lean-toolchain (full content): `leanprover/lean4:v4.34.0-rc1`

## Probe actually run (2026-09-01, this audit session)
1. Installed the pinned toolchain: `elan toolchain install
   leanprover/lean4:v4.34.0-rc1` -> "leanprover/lean4:v4.34.0-rc1 installed -
   Lean (version 4.34.0-rc1, arm64-apple-darwin24.6.0, commit
   3447a668783dbce1a8fdb97101dd067687b2b418, Release)".
2. mathlib checkout at the revision pinned in lake-manifest.json:
   `d0be1efe9afff6119115373bf4ea5abd833b3a95` (shallow fetch; HEAD verified:
   "HEAD is now at d0be1efe9a chore: lake shake --add-public --keep-implied
   --keep-prefix --fix (#42840)").
3. `lake exe cache get` -> "Decompressed 8711 file(s)", exit 0.
4. Clean workspace with the package's six source/config files verbatim:
   `lake build Tower Millennium` -> "Build completed successfully (8730
   jobs)." BUILD_EXIT=0.
5. `lake env lean print_axioms.lean` -> AXIOMS_EXIT=0, verbatim output:
```
'Millennium.riemannHypothesis_of_selfAdjoint_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.yang_mills_gap' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.ns_official' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.hodge_kunneth' depends on axioms: [propext]
'Millennium.bsd_official' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.P_neq_NP_of_proof_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```
6. Independent grep of the sources (this audit's lean_parser, comments
   stripped): 41 declarations, 0 live `sorry`, 0 `axiom` declarations.

Full receipt: `../../data/BUILD_RECEIPT.md`.

## Fair analysis
- The kernel claims are TRUE. Reproduced verbatim, independent toolchain and
  workspace. The package is honest about its build hygiene.
- The axioms listed are indeed the three foundational axioms of Lean/mathlib;
  `hodge_kunneth` depends only on `propext`, exactly as claimed.
- HOWEVER: kernel acceptance certifies that each term type-checks. It does
  not certify that the types say what the README says they say. F02-F08
  document that the types are tautologies, substitutions, list identities,
  or implications whose premises carry the open problems. Axiom-freedom of
  `0 < n + 1` is expected, not evidential.

## Verdict
CONFIRMED (the kernel claims are real) - and evidentially void for the
headline claim. The package does not misreport its kernel facts; it
over-interprets them. We dispute no kernel output; we dispute what it is
claimed to demonstrate.
