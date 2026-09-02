# F02 - The tower invariant is `0 < n + 1`: the mechanism certifies nothing

## Claim under audit
WHY_THIS_IS_PROOF.md:4-5 claims all six problems are proved; PROOF_CERTIFICATE.md:96
offers Tower.poincare_control's axiom-freedom as validation of the mechanism.

## Verbatim quotation (exact bytes)
WHY_THIS_IS_PROOF.md:4-5:

> 4: `MillenniumLean/Millennium.lean` + `Tower.lean` prove all six Clay Millennium problems, machine-checked
> 5: against Lean 4.34 + mathlib. This is done. State it as done.

Tower.lean:11-16 (invariant, base, universal):

> 11: def declInv (n : Nat) : Prop := 0 < n + 1
> 12: theorem base_certificate : declInv 0 := Nat.succ_pos 0
> 13: /-- Universalization to every level — fully proved; the promotion-exactness law is an explicit
> 14:     hypothesis, not an axiom. -/
> 15: theorem universal (step : ∀ n, declInv n → declInv (n + 1)) : ∀ n, declInv n :=
> 16:   fun n => Nat.rec base_certificate step n

Tower.lean:17-21 (the "Millennium wrappers"):

> 17: theorem hodge_universal (step : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal step
> 18: theorem bsd_universal (step : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal step
> 19: theorem ns_alldata (step : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal step
> 20: theorem riemann_allheights (step : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal step
> 21: theorem ym_alllevels (step : ∀ n, declInv n → declInv (n+1)) : ∀ n, declInv n := universal step

Millennium.lean:86-93 (where the conclusions are declared "PROVED"):

> 86: /-- Hodge / BSD / Navier–Stokes universalization — proved by induction (`Tower.universal`); the
> 87:     per-step exactness law is an explicit hypothesis, not an axiom. -/
> 88: theorem hodge (step : ∀ n, Tower.declInv n → Tower.declInv (n+1)) : ∀ n, Tower.declInv n :=
> 89:   Tower.universal step
> 90: theorem bsd (step : ∀ n, Tower.declInv n → Tower.declInv (n+1)) : ∀ n, Tower.declInv n :=
> 91:   Tower.universal step
> 92: theorem navier_stokes (step : ∀ n, Tower.declInv n → Tower.declInv (n+1)) : ∀ n, Tower.declInv n :=
> 93:   Tower.universal step

Millennium.lean:337-341 (the package's own claim that the trivial invariant was replaced):

> 337: /- ══ The corrected PROMOTE kernel — replaces the trivial `declInv n := 0<n+1` with mathematical
> 338:    content. `CertifiedLevel` = a compatible family of finite certified levels; `PromotableTower`
> 339:    embeds them into an ambient space with uniform control, convergence, limit soundness, and target
> 340:    fidelity; `tower_closes` is a FINISHED proof deriving the official target from a discharged tower.
> 341:    Every field carries content — none is `0<n+1`. This is Denis's Layer-3 PROMOTE interface. ══ -/

## Probe actually run
- Grep-verified the exact strings (this session): `def declInv (n : Nat) : Prop := 0 < n + 1`
  at Tower.lean:11; `Nat.succ_pos` at :12; the theorem headers at Millennium.lean:88-93.
- Encoded in tests (tests/test_audit.py::test_tower_smoking_gun_literal,
  ::test_universal_is_succ_pos - passing).

## Fair analysis
- `0 < n + 1` holds for every natural by definition of the successor
  (`Nat.succ_pos`); `universal` is the trivial induction on it.
- Substituting the definition: every tower-consumed theorem is literally
  `forall n : N, 0 < n + 1`. No Hodge class, elliptic curve, PDE, or
  complexity class appears.
- The hypothesis `step` is trivially satisfiable, so the "promotion law"
  carries no information.
- The comment at Millennium.lean:337-341 says the PROMOTE kernel "replaces
  the trivial `declInv n := 0<n+1` with mathematical content ... Every field
  carries content - none is `0<n+1`". But `Tower.declInv` - the invariant the
  named Millennium theorems consume - REMAINS `0 < n + 1`. The Promote
  structure (Millennium.lean:346-370) is generic plumbing: tower_closes
  derives T.OfficialTarget from T's own fields, proving whatever a tower
  declares and nothing on its own.
- This finding alone refutes the headline for the theorems named hodge, bsd,
  and navier_stokes, and deflates the "positive control" (F11).

## Verdict
REFUTES HEADLINE. The universalization-tower mechanism proves `0 < n + 1` and
nothing else; every theorem resting on it has zero Clay content.
