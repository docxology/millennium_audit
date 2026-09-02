# F04 - Yang-Mills: the "final theorem" is a substitution

## Claim under audit
README.md table row: "Yang-Mills existence and mass gap -> Millennium.yang_mills_gap".
WHY_THIS_IS_PROOF.md section 2 (lines 31-36) presents the twisted-Laplacian
lemmas as closing "Gap m > 0".

## Verbatim quotation (exact bytes)
WHY_THIS_IS_PROOF.md:31-36:

> 31: ## 2. Yang–Mills existence and mass gap
> 32: `ym_twisted_gap_uniform`: every mode of the ℤ₃-twisted continuum Laplacian is ≥ (2π/3ℓ)² > 0 — a bound
> 33: with **no lattice spacing in it**, uniform in the cutoff (the mass gap survives the continuum limit).
> 34: Mechanism: 2πn + 2π/3 = (2π/3)(3n+1), (3n+1)² ≥ 1 for every integer n. `ym_discrete_gap_tendsto`: the
> 35: discrete gap converges to k² as a→0 (real analysis). `ym_center_flux_pos`, `yang_mills_gap`,
> 36: `ym_flux_quantized` close the positivity and continuum identification. Gap m > 0.

Millennium.lean:81-84 (the named final, complete):

> 81: /-- Yang–Mills — the continuum gap is positive, proved: given the computed center-flux lower bound
> 82:     c > 0 (`ym_flux_quantized`-style) and the identification m = c (exact boundary composition), the
> 83:     continuum gap m is positive. Both premises are explicit hypotheses. -/
> 84: theorem yang_mills_gap (c m : ℝ) (hc : 0 < c) (hid : m = c) : 0 < m := hid ▸ hc

Millennium.lean:34-36 (the "quantization" support):

> 34: /-- Yang–Mills / center flux: a positive integer charge is ≥ 1 — a quantized lower bound
> 35:     cannot decay continuously to 0 under refinement. -/
> 36: theorem ym_flux_quantized (q : Nat) (h : 0 < q) : 1 ≤ q := h

Millennium.lean:121-128 (the "uniform gap" header):

> 121: /-- **Yang–Mills center-flux uniform lower bound, FINISHED — a real term.**
> 122:     For the ℤ₃-twisted continuum Laplacian −d²/dx² on a torus of physical size ℓ with quasi-periodic BC
> 123:     ψ(x+ℓ)=e^{i·2π/3}ψ(x), mode n ∈ ℤ has eigenvalue ((2πn + 2π/3)/ℓ)². EVERY mode is bounded below by
> 124:     (2π/(3ℓ))² > 0 — a bound with NO lattice spacing `a` in it, hence uniform in the cutoff. This is the
> 125:     corpus's `uniformBound` field (the companion computed corpus) as a kernel term.
> 126:     Mechanism: 2πn + 2π/3 = (2π/3)(3n+1) and (3n+1)² ≥ 1 for every integer n (3n+1 ≠ 0). -/
> 127: theorem ym_twisted_gap_uniform (ℓ : ℝ) (hℓ : 0 < ℓ) (n : ℤ) :
> 128:     (2 * Real.pi / (3 * ℓ)) ^ 2 ≤ ((2 * Real.pi * n + 2 * Real.pi / 3) / ℓ) ^ 2 := by

## Probe actually run
- Verified the exact line: `theorem yang_mills_gap (c m : ℝ) (hc : 0 < c) (hid : m = c) : 0 < m := hid ▸ hc`.
- Parsed binders via src/lean_parser.py: premises `hc`, `hid`;
  CONDITIONAL_IMPLICATION (data/audit_report.json).
- Axiom report from our independent reproduction matches the package.

## Fair analysis
- `hid ▸ hc` rewrites `0 < c` through `m = c`. That is the whole proof, and
  the type is its whole content: "if c is positive and m equals c, m is
  positive".
- The official Clay problem asks for EXISTENCE of quantum Yang-Mills theory
  on R4 for a compact simple gauge group, satisfying the Wightman axioms,
  WITH a positive mass gap. "Existence" is load-bearing: constructing the
  interacting quantum theory is the open, hard part. No Wightman axiom,
  gauge group, field strength, or lattice gauge theory appears in any type
  (grep: no `Wightman`, no `gauge` in any declaration type).
- The supporting lemmas are true, kernel-checked real analysis: the 1D
  twisted Laplacian spectrum bound (:127-138) and the discrete-gap limit
  (:155-194). These are facts about FREE scalar operators on a 1D torus; a
  free-field spectral gap has no logical bearing on existence of interacting
  4D gauge theory - the actual prize content.
- Precision note (red-team pass, verified against Millennium.lean:117-119):
  the two premises are NOT symmetric. `hc : 0 < c` is dischargeable - the
  package's own `ym_center_flux_pos : (0:R) < (2 * Real.pi / 3)^2 := by
  positivity` (:119) proves positivity unconditionally, and instantiating
  `c := (2*pi/3)^2` would discharge `hc`. The entire problem lives in
  `hid : m = c` - the continuum identification from quantum Yang-Mills data -
  which is wholly assumed. The verdict is unaffected: an implication whose
  load-bearing premise is assumed proves nothing about the prize. The
  package's own audit.py lists both as CONDITIONAL premises.

## Verdict
REFUTES HEADLINE. Substitution through an equation; the open problem is
absent from every type in the package.
