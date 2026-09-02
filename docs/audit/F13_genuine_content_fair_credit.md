# F13 - Genuine real content in the package (fair credit, itemized)

## Purpose
A fair audit itemizes what IS real. The following declarations are true,
kernel-checked, correctly anchored in mathlib. None bears Clay content
(F02-F08), but each is an honest small theorem or a faithful formalization.

## The itemized genuine content (exact bytes)

### About the real Riemann zeta function
Millennium.lean:54-58:

> 54: /-- A GENUINE theorem about the actual `riemannZeta`: its trivial zeros lie at −2(n+1). This is real
> 55:     content about the real object (mathlib `riemannZeta_neg_two_mul_nat_add_one`), the exceptions
> 56:     excluded in the `RiemannHypothesis` statement — a true fact about ζ. -/
> 57: theorem zeta_trivial_zero (n : ℕ) : riemannZeta (-2 * (n + 1)) = 0 :=
> 58:   riemannZeta_neg_two_mul_nat_add_one n

### Hermitian spectral theory
Millennium.lean:27-32:

> 27: /-- Riemann, machine-proved: a self-adjoint (Hermitian)
> 28:     operator has REAL spectrum. Every eigenvalue of a Hermitian matrix is real — mathlib's
> 29:     `Matrix.IsHermitian.eigenvalues` is ℝ-valued by construction. The spectral correspondence — that
> 30:     such an operator's spectrum equals the zeta ordinates — is the compiled core. -/
> 31: theorem hermitian_spectrum_real {n : Type*} [Fintype n] [DecidableEq n]
> 32:     {A : Matrix n n ℂ} (hA : A.IsHermitian) (i : n) : (hA.eigenvalues i : ℝ) = hA.eigenvalues i := rfl

### Real analysis (Yang-Mills supports)
Millennium.lean:127-138 (uniform twisted-Laplacian bound; ~12 lines of honest
nlinarith/omega analysis):

> 127: theorem ym_twisted_gap_uniform (ℓ : ℝ) (hℓ : 0 < ℓ) (n : ℤ) :
> 128:     (2 * Real.pi / (3 * ℓ)) ^ 2 ≤ ((2 * Real.pi * n + 2 * Real.pi / 3) / ℓ) ^ 2 := by
> 129:   have hℓ' : ℓ ≠ 0 := ne_of_gt hℓ
> 130:   have hk : (1 : ℤ) ≤ (3 * n + 1) ^ 2 := by
> 131:     have h0 : 3 * n + 1 ≤ -1 ∨ 1 ≤ 3 * n + 1 := by omega
> 132:     rcases h0 with h | h <;> nlinarith
> 133:   have hkr : (1 : ℝ) ≤ (3 * (n : ℝ) + 1) ^ 2 := by exact_mod_cast hk
> 134:   have key : ((2 * Real.pi * n + 2 * Real.pi / 3) / ℓ) ^ 2
> 135:            = (2 * Real.pi / (3 * ℓ)) ^ 2 * (3 * (n : ℝ) + 1) ^ 2 := by
> 136:     field_simp
> 137:   rw [key]
> 138:   nlinarith [sq_nonneg (2 * Real.pi / (3 * ℓ)), hkr]

Millennium.lean:150-156 (finite-to-limit bridge; ~45 lines of genuine
analysis via cos_two_mul, sin x / x -> 1):

> 150: open Filter Topology in
> 151: /-- **Yang–Mills `converges` field (Cycle C), FINISHED — real analysis.** As the lattice
> 152:     spacing `a → 0`, the discrete ℤ₃-twisted-Laplacian gap `(2/a²)(1 − cos(a·k))` converges to the
> 153:     continuum value `k²` for physical wavenumber `k`. Via `cos(a k) = 1 − 2 sin²(a k/2)` and `sin/·→1`.
> 154:     This is the finite→limit bridge carrying the discrete gap to the continuum value. -/
> 155: theorem ym_discrete_gap_tendsto (k : ℝ) :
> 156:     Tendsto (fun a : ℝ => (2 / a ^ 2) * (1 - Real.cos (a * k))) (𝓝[≠] (0 : ℝ)) (𝓝 (k ^ 2)) := by

### Faithful formalizations of official statements (defs, no proofs)
- ns_official (Millennium.lean:249-264) - faithful Clay NS statement (F05).
- bsd_official (Millennium.lean:205-211) - rank/vanishing statement (F06).
- hasZeroOfOrder (Millennium.lean:200-203) - genuine order-of-vanishing
  predicate.
- schwartzDecay (Millennium.lean:235-239) - every-derivative/every-weight
  Schwartz condition via iteratedFDeriv.
- solvesNS, divergence, vlaplace, convect (:216-247) - correct fderiv-based
  NS primitives.

### Correct generic plumbing and list algebra
- Promote.tower_closes (Millennium.lean:372-379) - fully generic
  "discharged tower proves its declared target": true plumbing, content-free
  alone.
- bsd_euler_multiplicative (:19-20) = List.prod_append;
  ns_enstrophy_additive (:24-25) = List.sum_append;
  bsd_universal_closed (:102-106) and ns_universal_closed (:110-114) - true
  commutative-monoid/monoid arithmetic by induction.

## Probe actually run
- Every quoted block read verbatim this session; axiom footprints reproduced
  independently (F01); binder parses recorded in data/audit_report.json.

## Fair analysis
- Sum: ~10 genuinely true small theorems, faithful statement formalizations
  (NS, BSD), correct plumbing, all kernel-clean. As formalization exercise,
  modest but real work.
- What none of it does: instantiate corr/bridge/hlb/hid for a real instance;
  prove any (p,p)-algebraicity; prove any regularity; construct any gauge
  theory; prove any proof-system lower bound.
- The pattern across F03-F12: every true theorem is (a) generic (lists,
  monoids, arbitrary towers), (b) a known fact about the trivial/easy part of
  a Millennium object (trivial zeros, free-field gaps, CP-products), or
  (c) a def of the open statement. The hard cores - the prizes - are
  uniformly absent.

## Verdict
CONFIRMED (fair credit). The package's real content is itemized and genuine;
none of it bears on the six Clay problems. Recorded so the audit cannot be
accused of denying the package's true positives.
