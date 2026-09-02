# F06 - Birch-Swinnerton-Dyer: a def of the conjecture, window-dressed with real mathlib objects

## Claim under audit
README.md table row: "Birch-Swinnerton-Dyer -> Millennium.bsd_official".
WHY_THIS_IS_PROOF.md section 5 (lines 49-53) concludes "Rank = order of
vanishing."

## Verbatim quotation (exact bytes)
WHY_THIS_IS_PROOF.md:49-53:

> 49: ## 5. Birch–Swinnerton-Dyer
> 50: `bsd_official`: the ℤ-rank of the real Mordell–Weil group `W.toAffine.Point` (= E(ℚ)) equals the order
> 51: of vanishing at s=1 of mathlib's elliptic `LSeries`, with the genuine analytic order-of-vanishing
> 52: predicate. `bsd_universal_closed`: the Euler product is multiplicative over any partition of local
> 53: factors, any depth, by induction. Rank = order of vanishing.

Millennium.lean:205-211 (bsd_official - a def, complete):

> 205: /-- The Birch–Swinnerton-Dyer target: the ℤ-rank of the Mordell–Weil group `W.toAffine.Point`
> 206:     (= E(ℚ)) equals the order of vanishing at s = 1 of the elliptic L-series `W.LSeries`. Both sides
> 207:     are mathlib's real objects, against a rational elliptic curve. `L` is required to BE mathlib's
> 208:     elliptic L-series — the exact Clay statement. -/
> 209: def bsd_official (W : WeierstrassCurve ℚ) [W.IsElliptic] [NumberField ℚ] (r : ℕ) (L : ℂ → ℂ)
> 210:     (_hL : L = fun s => WeierstrassCurve.LSeries W s) : Prop :=
> 211:   Module.finrank ℤ (W.toAffine.Point) = r ∧ hasZeroOfOrder L 1 r

Millennium.lean:200-203 (the analytic ingredient):

> 200: /-- Standard order-of-vanishing predicate (the real definition): `f` has a
> 201:     zero of order exactly `r` at `z₀` iff `f = (·−z₀)^r · g` locally with `g` analytic and `g z₀ ≠ 0`. -/
> 202: def hasZeroOfOrder (f : ℂ → ℂ) (z₀ : ℂ) (r : ℕ) : Prop :=
> 203:   ∃ g : ℂ → ℂ, AnalyticAt ℂ g z₀ ∧ g z₀ ≠ 0 ∧ ∀ᶠ s in nhds z₀, f s = (s - z₀) ^ r * g s

Millennium.lean:90-91 (the theorem named after the problem):

> 90: theorem bsd (step : ∀ n, Tower.declInv n → Tower.declInv (n+1)) : ∀ n, Tower.declInv n :=
> 91:   Tower.universal step

Millennium.lean:17-20 (the "Euler product" support):

> 17: /-- BSD / Euler product: the global L composes multiplicatively from local factors —
> 18:     the genuine general theorem `List.prod_append`, any commutative monoid (ℂ, ℝ, …). -/
> 19: theorem bsd_euler_multiplicative {M : Type*} [CommMonoid M] (l1 l2 : List M) :
> 20:     (l1 ++ l2).prod = l1.prod * l2.prod := List.prod_append

## Probe actually run
- Parsed kind: `def` (DEFINITION_ONLY in data/audit_report.json).
- Ran the package's own audit.py: BSD listed as "CONDITIONAL - premises: _hL"
  - the only premise is the constraint that L IS the elliptic L-series.
- Independent axiom report matches the package.

## Fair analysis
- Credit: the def targets the real mathlib objects (WeierstrassCurve.Point
  with its AddCommGroup instance; WeierstrassCurve.LSeries) and a genuine
  analytic order-of-vanishing predicate; `finrank Z (W.toAffine.Point)` is
  the honest algebraic-rank side. Competent statement-rendering.
- Gaps: (a) nothing proves rank = vanishing order for even ONE curve;
  (b) the official Clay formulation also requires the full leading
  coefficient formula (Tamagawa numbers, Sha, real period, regulator) -
  absent even as a def; (c) the premise `_hL` (L-series identity) is underscore-named
  AND never used in the definition body (it occurs only in its own binder,
  Millennium.lean:210; grep-verified) - the def does not even internally
  constrain `L` to be the elliptic L-series. The docstring (:207-208) claims
  "`L` is required to BE mathlib's elliptic L-series", but the definition
  leaves `L` a free function: the claimed constraint is not enforced. This
  strengthens the finding (red-team pass N01): the window dressing extends
  to the def's own premise, which is discarded entirely.
- The theorem `bsd` reduces to `0 < n + 1` (F02). `bsd_euler_multiplicative`
  is `List.prod_append` - true, about lists in a free commutative monoid,
  not about L-functions.
- The analytic continuation and functional equation of the elliptic L-series
  - prerequisites for speaking of vanishing order at s=1 in general - are
  not established anywhere in the package (and are not in mathlib at this
  pin); the package adds none.

## Verdict
REFUTES HEADLINE. A well-formed def of the conjecture plus trivial list
algebra; no rank/analytic-rank content proven for any curve.
