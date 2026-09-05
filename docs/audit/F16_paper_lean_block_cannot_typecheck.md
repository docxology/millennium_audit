# F16 - The paper's Section 4 block cannot typecheck against the shipped package (rebuttal pass)

## Claim under audit

Paper Section 4 (pp. 14-15) presents, as Lean source, the closed finals formed by consuming
certificates — e.g. `hodge_final : OfficialHodgeConjecture := gftqc_hodge_algebraic hodge_kunneth`.
Rebuttal comment: "the problem specific GFTQC certificates/invariants are then explicitly consumed
in those finals."

## Verbatim quotation (paper v1.0, §4, PDF text extraction)

```
theorem riemann_final : RiemannHypothesis :=
riemannHypothesis_of_selfAdjoint_correspondence
gftqc_operator
-- D
: the GFTQC-computed self-adjoint operator
gftqc_operator_selfAdjoint -- hD : IsSelfAdjoint D
(proved)
gftqc_corr
-- corr : the Hilbert–Pólya correspondence (proved)

theorem yang_mills_final : OfficialYangMillsStatement :=
...
gftqc_ym_official
-- 0 < m → OfficialYangMillsStatement (proved)
(yang_mills_gap gftqc_c gftqc_m gftqc_c_pos gftqc_m_eq_c) -- : 0 < gftqc_m
theorem navier_stokes_final : ∀ ν, 0 < ν → ns_official ν :=
fun ν hν => gftqc_ns_global ν hν
-- global-existence certificate (proved)
theorem hodge_final : OfficialHodgeConjecture :=
gftqc_hodge_algebraic hodge_kunneth
-- algebraicity certificate (proved)
theorem bsd_final : OfficialBSDConjecture :=
gftqc_bsd_rank_eq_order gftqc_Lseries gftqc_rank_cert -- rank↔order (proved)
theorem p_neq_np_final : P_neq_NP StandardComplexityModel :=
P_neq_NP_of_proof_lower_bound StandardComplexityModel gftqc_hard_problem
gftqc_np_complete gftqc_size gftqc_hlb gftqc_bridge -- hlb, bridge (proved)
```

## Probe actually run (2026-09-04)

1. **Absent-symbol census.** The block requires, beyond the shipped helpers, at minimum:
   `gftqc_operator`, `gftqc_operator_selfAdjoint`, `gftqc_corr`, `OfficialYangMillsStatement`,
   `gftqc_ym_official`, `gftqc_c`, `gftqc_m`, `gftqc_c_pos`, `gftqc_m_eq_c`, `gftqc_ns_global`,
   `gftqc_bsd_rank_eq_order`, `gftqc_Lseries`, `gftqc_rank_cert`, `StandardComplexityModel`,
   `gftqc_hard_problem`, `gftqc_np_complete`, `gftqc_size`, `gftqc_hlb`, `gftqc_bridge` —
   22 identifiers, **zero** of which occur anywhere in the package (grep receipts, F15) —
   `ComplexityModel` and `P_neq_NP` do exist there; what is missing is precisely the instantiation
   data (`StandardComplexityModel`, the `gftqc_*` terms).
2. **Known-type impossibility (Hodge).** The one consumed theorem whose shipped type is fixed is
   `hodge_kunneth`:

> 45: theorem hodge_kunneth : conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1] := by decide

   The paper itself annotates it "(proved by decide)" and calls the CP3 x CP2 match "validation"
   (§10). A certificate `gftqc_hodge_algebraic` accepting that decidable list identity as its sole
   argument and returning `OfficialHodgeConjecture` cannot express Theorem 10.7's claimed content
   (universality over every smooth projective variety): its hypothesis quantifies over nothing. If
   it typechecked, `OfficialHodgeConjecture` would be a junk proposition derivable from list
   arithmetic — provable in zero lines by the same decide (see F18/F19 for the pattern).
3. **Mathlib anchor census.** At the pinned mathlib revision (lake-manifest d0be1efe…): `grep -ril
   hodge` hits only `ModelTheory/Fraisse.lean` — whose match is the model theorist's surname
   "Hodges" in a bibliography, not Hodge theory — and two p-adic files (FontaineTheta, BDeRham);
   `grep -rl Chow`: **zero** files. There is no Hodge-conjecture statement, no Chow group of
   algebraic cycles, no `OfficialHodgeConjecture` for a faithful type to reuse — unlike RH, where
   mathlib's real `RiemannHypothesis` exists (F07 credit).
4. **Self-undermining annotations.** `gftqc_ns_global` is annotated "(proved)" at type
   `∀ ν, 0 < ν → ns_official ν` — that single term IS the Clay Navier-Stokes theorem (global
   smooth solutions for every admissible Schwartz datum, plus uniqueness). Renaming the open
   theorem a "certificate" relocates the assumption; it does not discharge it. The same holds for
   `gftqc_ym_official : 0 < m → OfficialYangMillsStatement (proved)` — a proved implication from
   bare positivity to the official Yang-Mills statement would already be the mass-gap theorem,
   consumed alongside the F04 substitution lemma.

## Fair analysis

- If a future package revision actually defines `gftqc_*` as proved theorems of these types, the
  audit re-runs and F15-F17 update. As of the md5-pinned deposit, the block is prose with Lean
  syntax: it names 22+ undeclared identifiers, and its two checkable applications cannot carry the
  claimed official content.
- The shipped helpers the paper names (riemannHypothesis_of_selfAdjoint_correspondence,
  yang_mills_gap, hodge_kunneth, ns_official, bsd_official, P_neq_NP_of_proof_lower_bound) are
  real — they are the audited F03-F08 objects.

## Verdict

REFUTES HEADLINE. The Section-4 block that the rebuttal designates as "the actual closed final
theorems" does not, and as typed cannot, exist against the published package.
