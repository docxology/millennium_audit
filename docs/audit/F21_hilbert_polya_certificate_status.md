# F21 - The Riemann certificate `gftqc_corr` is the Hilbert–Pólya binder restated (rebuttal pass)

## Claim under audit

Rebuttal comment: "For RH, gftqc_corr [is] tantam[ount]ed into riemann_final." Paper §4: "gftqc_corr
is a proved theorem in the package, instantiated into the closed riemann_final, not a parameter of
a displayed helper."

## Verbatim quotation (paper v1.0, §7.1 and construction paragraph, PDF text extraction)

```
On the encoded register the governed computation returns the first 300 ordinates {tn} ... each
self-certified by a Hardy-Z residual at the 10^-13 level, and their normalized nearest-neighbour
spacings reproduce the Gaussian Unitary Ensemble law (empirical mean spacing 1.004; Lemma 7.4) ...

The single certificate consumed from that computation is the correspondence gftqc_corr:

7.1    ζ(ρ) = 0, ρ nontrivial, ρ ≠ 1 ⟹ ∃ z ∈ spec(D), ρ = 1/2 + i z.
```

## Probe actually run (2026-09-04)

1. Package census (F15): no `gftqc_corr`, no `gftqc_operator`, no ordinates table, no Berry-Keating
   operator construction — zero hits.
2. Type comparison against the shipped final:

> 70: theorem riemannHypothesis_of_selfAdjoint_correspondence
> 71:     {A : Type*} [CStarAlgebra A] (D : A) (hD : IsSelfAdjoint D)
> 72:     (corr : ∀ ρ : ℂ, riemannZeta ρ = 0 → (¬ ∃ n : ℕ, ρ = -2 * (n + 1)) → ρ ≠ 1 →
> 73:         ∃ z ∈ spectrum ℂ D, ρ = ((1 / 2 : ℝ) : ℂ) + Complex.I * z) :

   The paper's 7.1 and the package's `corr` binder (Millennium.lean:72-73) are the same proposition:
   every nontrivial zero of ζ lies in the spectrum of D. The paper's claim that this proposition is
   "a proved theorem in the package" is contradicted by the package itself, which carries it only
   as an unproved premise binder (F07).

## Fair analysis

- The two artifacts are at least mutually consistent about WHAT the decisive object is: the
  Hilbert–Pólya correspondence. The dispute is its status. Proving 7.1 for a concrete self-adjoint
  D whose spectrum contains all nontrivial zero ordinates is the open problem; a Lean proof of it
  would close `riemannHypothesis_of_selfAdjoint_correspondence` and constitute the million-dollar
  proof. No such term exists in the deposit.
- The paper's numeric validation (300 ordinates, Hardy-Z residual ≤ 1e-13, GUE spacing mean 1.004)
  is evidence of a kind — finite verification in the spirit of Platt-Trudgian's verified RH up to
  height 3·10^12 — but (a) it ships in no verifiable artifact (neither the package nor any
  committed data), (b) a finite prefix of ordinates cannot instantiate the ∀ρ premise, and (c)
  "self-certified" residuals are the claim under test, not independent verification. The paper's
  own framing ("the first 100 used for the finite completeness demonstration, Lemma 7.3") concedes
  the finite scope.
- Credit preserved (F07/F13): the shipped conditional theorem and its real-part forcing via
  `IsSelfAdjoint.mem_spectrum_eq_re` are correct and mathlib-anchored; `zeta_trivial_zero` is real
  content about the real zeta. None of it changes the status of `corr`.

## Verdict

REFUTES HEADLINE. The certificate the rebuttal says is "tantamount[ed] into riemann_final" is, in
the only published artifact, exactly the unproved Hilbert–Pólya premise binder (F07); no
`gftqc_corr` term, operator, or ordinate data ship anywhere in the verifiable layer.
