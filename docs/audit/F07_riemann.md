# F07 - Riemann Hypothesis: conditional on exactly the open problem

## Claim under audit
README.md table row: "Riemann Hypothesis -> Millennium.riemannHypothesis_of_selfAdjoint_correspondence".
WHY_THIS_IS_PROOF.md section 1 presents the Hilbert-Polya reduction as "non-circular".

## Verbatim quotation (line-anchored, exact bytes)

Millennium.lean:70-79 (the named final, complete):

> 70: theorem riemannHypothesis_of_selfAdjoint_correspondence
> 71:     {A : Type*} [CStarAlgebra A] (D : A) (hD : IsSelfAdjoint D)
> 72:     (corr : ∀ ρ : ℂ, riemannZeta ρ = 0 → (¬ ∃ n : ℕ, ρ = -2 * (n + 1)) → ρ ≠ 1 →
> 73:         ∃ z ∈ spectrum ℂ D, ρ = ((1 / 2 : ℝ) : ℂ) + Complex.I * z) :
> 74:     RiemannHypothesis := by
> 75:   intro ρ hz hntriv hne
> 76:   obtain ⟨z, hzspec, hρ⟩ := corr ρ hz hntriv hne
> 77:   have him : z.im = 0 := by rw [hD.mem_spectrum_eq_re hzspec]; simp
> 78:   rw [hρ]
> 79:   simp [Complex.add_re, Complex.mul_re, Complex.I_re, Complex.I_im, him]

Millennium.lean:63-69 (the package's fairness argument in its own docstring):

> 63: /-- **RH integration socket — the non-circular Hilbert–Pólya reduction.** Provider fields:
> 64:     a self-adjoint element `D` of a C⋆-algebra, and a spectral correspondence `corr` sending every
> 65:     nontrivial zero `ρ` of the REAL `riemannZeta` to `ρ = ½ + i·z` with `z ∈ spectrum ℂ D`. Given
> 66:     both, mathlib's `RiemannHypothesis` follows. Crucially `corr` does NOT assume `Re ρ = ½`; the real
> 67:     part is FORCED by mathlib's `IsSelfAdjoint.mem_spectrum_eq_re` (self-adjoint ⟹ real spectrum) — so
> 68:     this is not circular. With the provider `(D, hD, corr)` supplied, `RiemannHypothesis` closes with
> 69:     no `sorry`/axiom. -/

Millennium.lean:54-58 (genuine content about the real zeta function):

> 54: /-- A GENUINE theorem about the actual `riemannZeta`: its trivial zeros lie at −2(n+1). This is real
> 55:     content about the real object (mathlib `riemannZeta_neg_two_mul_nat_add_one`), the exceptions
> 56:     excluded in the `RiemannHypothesis` statement — a true fact about ζ. -/
> 57: theorem zeta_trivial_zero (n : ℕ) : riemannZeta (-2 * (n + 1)) = 0 :=
> 58:   riemannZeta_neg_two_mul_nat_add_one n

## Probe actually run
- Parsed binders: premises `hD`, `corr` (CONDITIONAL_IMPLICATION in
  ../../data/audit_report.json, matching the package's own audit.py output).
- Verified the proof body: after `corr` fires, only real-part arithmetic
  remains (lines 75-79 above).
- Independent `#print axioms` reproduction matches the package verbatim (F01).

## Fair analysis
- Credit: the implication is genuinely proved and the mathlib anchors are
  real: `RiemannHypothesis` is mathlib's actual statement about the real
  `riemannZeta`, and `IsSelfAdjoint.mem_spectrum_eq_re` is a real mathlib
  lemma (line 77). The 5-tactic proof is correct: if every nontrivial zero is
  1/2 + i*z with z in the spectrum of a SELF-ADJOINT operator, z is real
  (self-adjoint spectra are real), so Re(rho) = 1/2.
- The "not circular" defense (lines 66-68) is technically accurate but misses
  the point: proving RH GIVEN corr is easy arithmetic. Constructing a
  self-adjoint D whose spectrum contains the imaginary parts of all
  nontrivial zeta zeros - the Hilbert-Polya program - is the open problem,
  and it appears only as an unproved premise binder. `corr` asserts, for
  every nontrivial zero, exactly the spectral-location fact whose derivation
  is the entire difficulty.
- Logical form: (HilbertPolya(D) AND correspondence) -> RH. The package
  proves the arrow. No D, hD, or corr term for the actual zeta zeros is
  provided; such a term would itself constitute the proof.
- `zeta_trivial_zero` (lines 57-58) is real mathlib content - true, and
  irrelevant to RH, which is about NONtrivial zeros (excluded by the
  hypothesis at line 72).
- Additional detail (red-team pass N02): `riemann_official` (line 52,
  `def riemann_official : Prop := RiemannHypothesis`) is a def alias of
  mathlib's statement with NO consuming theorem - the same DEFINITION_ONLY
  category this audit assigns to ns_official/bsd_official. The "official"
  alias itself is proof-free; only the conditional theorem above exists.

## Verdict
REFUTES HEADLINE. A kernel-checked implication whose premise is the open
problem restated; the hard part is assumed, not proved.
