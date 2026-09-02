# Results

## Kernel hygiene: confirmed (F01)

Independently reproduced: clean build (exit 0), zero live `sorry`, zero
project axioms, and the six axiom footprints byte-identical to the package's
committed receipt - e.g. `Millennium.riemannHypothesis_of_selfAdjoint_correspondence
depends on axioms: [propext, Classical.choice, Quot.sound]`, and
`Millennium.hodge_kunneth depends on axioms: [propext]`.

## The tower: one trivial invariant under five names (F02)

Tower.lean:11 defines `declInv (n : Nat) : Prop := 0 < n + 1`; Tower.lean:12
grounds it in `Nat.succ_pos 0`; Tower.lean:15-16 builds `universal` as plain
induction. The theorems named `hodge`, `bsd`, and `navier_stokes`
(Millennium.lean:88-93), the five Tower wrappers (:17-21), and
`poincare_control` (:26) all reduce to `forall n : N, 0 < n + 1`. No Hodge
class, elliptic curve, PDE, or complexity class appears.

## Per-problem verdicts

1. **Riemann (F07).** `riemannHypothesis_of_selfAdjoint_correspondence`
   (Millennium.lean:70-79) is a correct 5-tactic proof of
   (self-adjoint D with the Hilbert-Polya correspondence corr) ->
   RiemannHypothesis. The premise `corr` asserts, for every nontrivial zeta
   zero, exactly the spectral-location fact whose construction is the open
   problem. No D or corr term is provided. CONDITIONAL_IMPLICATION.
2. **Yang-Mills (F04).** `yang_mills_gap (c m : R) (hc : 0 < c) (hid : m = c)
   : 0 < m := hid ▸ hc` (Millennium.lean:84): substitution. No gauge theory,
   no Wightman axioms, no existence content anywhere. CONDITIONAL_IMPLICATION.
3. **Navier-Stokes (F05).** `ns_official` (Millennium.lean:254-264) is a
   faithful def of the Clay statement - real mathlib analysis objects,
   Schwartz decay, uniqueness - but a def proves nothing; the theorem named
   `navier_stokes` is the tower tautology. DEFINITION_ONLY.
4. **Hodge (F03).** `hodge_kunneth : conv [1,1,1,1] [1,1,1] =
   [1,2,3,3,2,1] := by decide` (Millennium.lean:45): a Hodge-diamond list
   computation for CP3 x CP2. The conjecture quantifies over all smooth
   projective varieties and concerns algebraicity of (p,p) classes; no
   variety, cohomology, or cycle object appears in any type.
   OFF_TOPIC_THEOREM.
5. **BSD (F06).** `bsd_official` (Millennium.lean:209-211) defines rank =
   vanishing order against real mathlib objects; nothing proves it for any
   curve, and the official leading-coefficient formula is absent even as a
   def. DEFINITION_ONLY.
6. **P vs NP (F08).** `P_neq_NP_of_proof_lower_bound` (Millennium.lean:324-333)
   is a correct 4-line contradiction from two premises that restate the
   conjecture: an unconditional superpolynomial proof-system lower bound
   (beyond current knowledge, as stated) and the proof-complexity-to-
   algorithm bridge (never achieved). `NPcomplete` is an uninterpreted
   interface field. CONDITIONAL_IMPLICATION.

## Cross-cutting findings

- **audit.py category error (F09).** The package's committed audit labels
  defs of open problems "CLOSED (no premise in the type)"; its premise
  detector works by binder NAME (h-prefix, corr/bridge/step) and silently
  counts unproved hypotheses like `size` as "data".
- **Axiom-footprint rhetoric (F10).** PROOF_CERTIFICATE.md:37-38 claims
  smuggled premises "would appear here as an extra axiom. It does not."
  False as an argument: premises are binder types, invisible to
  `#print axioms`. The conditional finals themselves are the counterexample.
- **Poincare "positive control" (F11).** The control's type is the same
  tautology `0 < n + 1`; a control that cannot fail validates nothing. No
  negative control exists.
- **Toy-but-true cluster (F12).** Klein ZMod-12 torsion and `2 < sqrt 5` are
  true and kernel-checked; the Clay-relevant objects live only in comments.
- **Genuine content (F13).** Roughly ten true small theorems (trivial zeta
  zeros, Hermitian spectrum reality, twisted-Laplacian bounds, discrete-gap
  convergence), two faithful statement formalizations, correct plumbing - all
  kernel-clean, none Clay-bearing.
- **External record (F14).** Context only: the companion paper's FTQC claims
  were publicly demolished (code distance 1; hidden post-selection;
  self-described "engineered signature"); the honest Lean formalization
  community marks all seven problems OPEN. The verdict above does not depend
  on any of this.
