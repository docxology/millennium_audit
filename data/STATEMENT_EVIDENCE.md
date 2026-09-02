# Per-Problem Statement Evidence (file:line anchored)

All line numbers verified against package/MillenniumLean/ in this session.

## 1. Riemann Hypothesis
- Claimed: `Millennium.riemannHypothesis_of_selfAdjoint_correspondence` (Millennium.lean:70-79)
- Type: `(D : A) (hD : IsSelfAdjoint D) (corr : forall rho, riemannZeta rho = 0 -> nontrivial -> exists z in spectrum C D, rho = 1/2 + i*z) -> RiemannHypothesis`
- Gap: `corr` IS the Hilbert-Polya correspondence - the open problem, assumed.
  Given it, lines 74-79 are ~5 tactic lines of real-part arithmetic. The
  package constructs no operator D and no correspondence. (The genuine
  mathlib anchors - RiemannHypothesis, riemannZeta - are real, which makes
  the shell respectable-looking.)
- Extra content that IS real: zeta_trivial_zero (Millennium.lean:57-58) - a
  true mathlib fact about trivial zeros, irrelevant to RH itself.

## 2. Yang-Mills existence and mass gap
- Claimed: `Millennium.yang_mills_gap` (Millennium.lean:84)
- Type: `theorem yang_mills_gap (c m : R) (hc : 0 < c) (hid : m = c) : 0 < m := hid > hc`
- Gap: LITERALLY a rewrite of `0 < c` through `m = c`. The entire Clay
  content (existence of 4D quantum Yang-Mills under Wightman axioms +
  positive mass gap) is absent. Supporting lemmas are true trivial facts
  about a 1D twisted Laplacian (Millennium.lean:127-138, 155-194); free-field
  spectral gaps say nothing about interacting 4D gauge theory. The Clay
  problem is existence of the interacting quantum theory - the hardest part -
  and it never appears in any type.

## 3. Navier-Stokes
- Claimed: `Millennium.ns_official` (Millennium.lean:254-264) - a def.
- Gap: The definition is a faithful rendering of the Clay statement (real
  analysis objects, Schwartz class, uniqueness). But a def proves nothing.
  The package audit.py calls this "CLOSED (no premise in the type)" - a
  category error: closedness of a def binder list is meaningless for
  proving. The theorem `navier_stokes` (Millennium.lean:92-93) =
  Tower.universal over `declInv n := 0 < n + 1`. NO global-regularity
  content exists anywhere in the package.

## 4. Hodge conjecture
- Claimed: `Millennium.hodge_kunneth` (Millennium.lean:42-45)
- Type: `conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1]` by decide.
- Gap: A Hodge-diamond computation for one variety (CP3 x CP2) by list
  convolution. The Hodge conjecture quantifies over all smooth projective
  varieties; the (p,p)-algebraicity question never appears in any type.
  WHY_THIS_IS_PROOF.md claims "Every (k,k)-class on projective space is
  algebraic - Hodge holds by direct construction" - asserted nowhere in the
  Lean sources; no algebraic-cycle machinery is present.

## 5. Birch-Swinnerton-Dyer
- Claimed: `Millennium.bsd_official` (Millennium.lean:209-211) - a def.
- Gap: defines rank = order-of-vanishing against real mathlib objects
  (WeierstrassCurve.Point, LSeries) - nice rendering, zero proof. The theorem
  `bsd` (Millennium.lean:90-91) reduces to the trivial tower invariant.
  (The official Clay statement also requires the full Tamagawa/Sha
  leading-coefficient formula, absent here even as a def.)

## 6. P vs NP
- Claimed: `Millennium.P_neq_NP_of_proof_lower_bound` (Millennium.lean:324-333)
- Type: premises hlb (unconditional superpolynomial proof-system lower
  bound) and bridge (proof-complexity -> algorithmic hardness transfer).
- Gap: 4-tactic-line diagonalization from premises that ARE the problem.
  Known width lower bounds give exponential size for resolution on random
  3CNF, but transfer to P != NP requires lower bounds for systems capturing
  all of P - exactly the open problem, assumed in `bridge`.

## Tower mechanism (all "universalizations")
- Tower.lean:11: `def declInv (n : Nat) : Prop := 0 < n + 1`
- Tower.lean:15-16: `universal` = Nat.rec over base `Nat.succ_pos 0`.
- Consumed as: hodge (Millennium.lean:88-89), bsd (:90-91),
  navier_stokes (:92-93), plus Tower wrappers (Tower.lean:17-21) and
  poincare_control (Tower.lean:26).
- Meaning: every one proves only `forall n : N, 0 < n + 1`. The Poincare
  "positive control" proving `0 < n+1` "through the identical mechanism" is
  itself the confession: the mechanism certifies nothing.
