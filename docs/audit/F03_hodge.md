# F03 - Hodge conjecture: the "final theorem" is list arithmetic

## Claim under audit
WHY_THIS_IS_PROOF.md section 4 (lines 45-48) claims `hodge_kunneth` plus the
prose assertion "Every (k,k)-class on projective space is algebraic - Hodge
holds by direct construction."

## Verbatim quotation (exact bytes)
WHY_THIS_IS_PROOF.md:45-48:

> 45: ## 4. Hodge conjecture
> 46: `hodge_kunneth`: the (k,k) Künneth count on ℂP³×ℂP² is exactly [1,2,3,3,2,1] by `decide` (kernel
> 47: arithmetic). Every (k,k)-class on projective space is algebraic — Hodge holds by direct construction.
> 48: 

Millennium.lean:41-45 (the entire Hodge content):

> 41: /-- Hodge / Künneth (concrete): h^{k,k}(CP^3 × CP^2) convolution = [1,2,3,3,2,1]. -/
> 42: def conv (a b : List Nat) : List Nat :=
> 43:   (List.range (a.length + b.length - 1)).map (fun k =>
> 44:     ((List.range (k+1)).map (fun i => (a.getD i 0) * (b.getD (k - i) 0))).foldl (· + ·) 0)
> 45: theorem hodge_kunneth : conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1] := by decide

## Probe actually run
- Verified the exact source line: `theorem hodge_kunneth : conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1] := by decide`.
- Independent `#print axioms Millennium.hodge_kunneth`: `depends on axioms: [propext]`
  (consistent with the package certificate).
- Grep across both .lean files for the terms any Hodge statement requires:
  `algebraic`, `cycle`, `cohomology`, `projective` - none occurs in any
  declaration TYPE (only in comments/prose).

## Fair analysis
- The theorem is TRUE and kernel-checked: the list convolution of the Hodge
  numbers of CP3 and CP2 equals [1,2,3,3,2,1]. `decide` leaves no doubt.
- But the official Clay statement quantifies over ALL smooth projective
  varieties over C: every rational (p,p) Hodge class is a rational linear
  combination of algebraic cycle classes. The package's theorem:
  (a) covers one specific product of projective spaces, not all varieties;
  (b) computes Hodge NUMBERS (dimensions), not Hodge CLASSES;
  (c) contains no algebraic-cycle space, no cycle classes, no variety type -
      the type is about `List Nat`.
- The sentence "Every (k,k)-class on projective space is algebraic - Hodge
  holds by direct construction" (WHY_THIS_IS_PROOF.md:47) has NO supporting
  declaration anywhere in the Lean sources. We grepped: no theorem states or
  proves algebraicity of any Hodge class. Prose claim, no formal referent.
- Fair note: algebraicity for products of projective spaces IS a true theorem
  of algebraic geometry (explicit cycle construction), so the prose direction
  is not mathematically false - it is simply not formalized here, and even
  formalized it would not cover the all-varieties statement the prize
  requires.

## Verdict
REFUTES HEADLINE (coverage). A true, kernel-checked list identity; the Hodge
conjecture's content never appears in any type.
