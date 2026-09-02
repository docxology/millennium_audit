# F05 - Navier-Stokes: a faithful DEF of the open problem, and no proof

## Claim under audit
README.md table row: "Navier-Stokes existence and smoothness -> Millennium.ns_official".
WHY_THIS_IS_PROOF.md section 3 (lines 38-43) claims the Clay statement plus
"Smooth for all time, no blow-up."

## Verbatim quotation (exact bytes)
WHY_THIS_IS_PROOF.md:38-43:

> 38: ## 3. Navier–Stokes global regularity
> 39: `ns_official` is the Clay statement in mathlib's real analysis: for ν>0 and every smooth,
> 40: divergence-free, Schwartz-decaying u₀ on ℝ³, global-in-time smooth (u,p) solving the incompressible NS
> 41: equations with u(0)=u₀, velocity unique — `solvesNS`/`divergence`/`vlaplace`/`convect` all via `fderiv`.
> 42: `ns_universal_closed`: enstrophy production additive over any subdomain partition, any depth, by
> 43: induction. Smooth for all time, no blow-up.

Millennium.lean:249-264 (ns_official - note `def`, not `theorem`):

> 249: /-- The Navier–Stokes global-regularity target: for viscosity ν > 0 and every
> 250:     smooth, divergence-free, rapidly-decaying initial field u₀ on ℝ³, there EXIST global-in-time fields
> 251:     (u,p) that are smooth in space for all t ≥ 0, smooth in time, have smooth pressure, satisfy the
> 252:     incompressible NS equations with u(0,·)=u₀, and the velocity is UNIQUE. Stated against mathlib's
> 253:     real `ContDiff`/`fderiv`/`gradient` — the exact Clay statement. -/
> 254: def ns_official (ν : ℝ) : Prop :=
> 255:   0 < ν → ∀ u₀ : NSVel → NSVel,
> 256:     ContDiff ℝ (⊤ : ℕ∞) u₀ → (∀ x, divergence u₀ x = 0) → schwartzDecay u₀ →
> 257:     ∃ (u : ℝ → NSVel → NSVel) (p : ℝ → NSVel → ℝ),
> 258:       (∀ t, 0 ≤ t → ContDiff ℝ (⊤ : ℕ∞) (u t)) ∧                    -- spatial smoothness, forward time
> 259:       (∀ x, ContDiffOn ℝ (⊤ : ℕ∞) (fun t => u t x) (Set.Ici 0)) ∧   -- temporal smoothness on t ≥ 0
> 260:       (∀ t, 0 ≤ t → ContDiff ℝ (⊤ : ℕ∞) (p t)) ∧                    -- pressure smoothness
> 261:       u 0 = u₀ ∧ solvesNS ν u p ∧
> 262:       (∀ u' p', (∀ t, 0 ≤ t → ContDiff ℝ (⊤ : ℕ∞) (u' t)) →
> 263:         (∀ x, ContDiffOn ℝ (⊤ : ℕ∞) (fun t => u' t x) (Set.Ici 0)) →  -- SAME solution class as u
> 264:         u' 0 = u₀ → solvesNS ν u' p' → u' = u)                       -- uniqueness of the velocity field

Millennium.lean:92-93 (the theorem named after the problem):

> 92: theorem navier_stokes (step : ∀ n, Tower.declInv n → Tower.declInv (n+1)) : ∀ n, Tower.declInv n :=
> 93:   Tower.universal step

Millennium.lean:104-111 (the "UNCONDITIONAL" discharge):

> 104:   induction blocks with
> 105:   | nil => simp
> 106:   | cons a t ih => rw [List.flatten_cons, List.prod_append, ih, List.map_cons, List.prod_cons]
> 107: 
> 108: /-- Navier–Stokes composition invariant, UNCONDITIONAL: enstrophy production over ANY subdomain
> 109:     partition (any depth) is additive. `step` discharged to a theorem, no hypothesis. -/
> 110: theorem ns_universal_closed {M : Type*} [AddCommMonoid M] (blocks : List (List M)) :
> 111:     blocks.flatten.sum = (blocks.map List.sum).sum := by

## Probe actually run
- Parsed the declaration kind: `def`, not `theorem` (src/lean_parser.py;
  DEFINITION_ONLY in data/audit_report.json).
- Ran the package's own audit.py (real execution): reproduces its committed
  classification of Navier-Stokes as CLOSED (see F09).
- Grep: no declaration proves any instance of ns_official or any
  global-regularity statement. The only declarations mentioning NS objects
  are the defs themselves (:216-247).

## Fair analysis
- Credit: the def is a faithful, careful rendering of the Clay statement
  using real mathlib analysis objects (fderiv, ContDiff, iteratedFDeriv
  Schwartz decay, forward-time smoothness, velocity uniqueness). Whoever
  wrote it understood the problem. Accurate formalization of an open
  conjecture is a real service.
- But a def of an open conjecture has NO proof value: stating
  `ns_official : Prop` proves nothing, exactly as writing the conjecture on
  paper proves nothing. The prize requires a term of this type (or its
  negation); none exists.
- The theorem `navier_stokes` reduces to `forall n, 0 < n + 1` (F02).
- `ns_universal_closed` - enstrophy-additivity over list partitions - is
  true, axiom-clean, and unrelated to regularity.
- The category error in the package's own audit (F09) - "CLOSED (no premise
  in the type)" for a def - is what lets this def masquerade as a result.

## Verdict
REFUTES HEADLINE. A correct formalization of the question is not an answer
to it; no global-regularity content exists anywhere in the package.
