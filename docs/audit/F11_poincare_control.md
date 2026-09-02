# F11 - The "Poincare positive control" is self-defeating

## Claim under audit
README.md (package description) presents Tower.poincare_control as a positive
control: the mechanism run on known truth (Perelman 2003).

## Verbatim quotation (exact bytes)
README.md:31-34:

> 31:   `lean-toolchain` and installs the exact compiler this project pins
> 32:   (`leanprover/lean4:v4.34.0-rc1`) automatically.
> 33: 
> 34: Install elan (one line, macOS/Linux):

Tower.lean:11 (the invariant the control consumes):

> 11: def declInv (n : Nat) : Prop := 0 < n + 1

Tower.lean:23-26 (control framing and theorem):

> 23: /-- Poincaré POSITIVE CONTROL (already-established truth, Perelman 2003): the governed round-S³ limit profile
> 24:     certificate, consumed the same way the six consume theirs. A control on known truth; NOT one of the
> 25:     six certified results. -/
> 26: theorem poincare_control (attr : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal attr

PROOF_CERTIFICATE.md:96:

> 96: Tower.poincare_control                            does not depend on any axioms                          ∅   (positive control: Perelman 2003, known truth)

## Probe actually run
- Verified all source lines by direct read (this session).
- Unfolded the statement: poincare_control attr = universal attr = fun n =>
  Nat.rec (Nat.succ_pos 0) attr n; after unfolding declInv its type is
  `forall n : N, 0 < n + 1`.

## Fair analysis
- Positive controls are sound methodology in general: certify a known-true
  statement; failure would indict the pipeline.
- The implementation defeats the purpose: the control's type is `0 < n + 1`,
  provable with zero premises in one tactic. Any pipeline - sound or not -
  certifies it. A control that cannot fail carries zero information about
  mathematical validity (its only real function is an end-to-end
  build/toolchain smoke test, which the kernel receipts of F01 already
  establish independently). A meaningful companion would be a NEGATIVE control (a
  known-false statement) to confirm rejection; the package has none.
- What the control actually demonstrates: the identical mechanism certifies
  `0 < n+1`, `conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1]`, and
  `0 < c -> m = c -> 0 < m`. That selectivity validates nothing about
  mathematical content.
- Credit: the package correctly notes the control is NOT one of the six
  certified results. The problem is the inference it invites: control passed,
  therefore mechanism valid, therefore the six are proved.

## Verdict
SELF-DEFEATING (as validation). A tautological positive control validates
nothing; read honestly, it shows the mechanism certifies tautologies as
readily as theorems.
