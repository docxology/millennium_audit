# F10 - The axiom-footprint argument: "premises would appear as axioms" is false

## Claim under audit
PROOF_CERTIFICATE.md:36-38 and 103-105 (quoted below).

## Verbatim quotation (exact bytes)
PROOF_CERTIFICATE.md:36-38:

> 36: **No theorem below depends on anything else.** In particular: no `sorryAx` (there is no `sorry`), and no
> 37: project-specific axiom. If any premise were smuggled in as an assumption, it would appear here as an extra
> 38: axiom. It does not. The footprint is the same three (or fewer) that underlie all of mathlib.

PROOF_CERTIFICATE.md:101-105:

> 101: Two independent kernel checks (`lake build` replay + `lake env lean` fresh elaboration) both exit 0 with no
> 102: errors. Every theorem's transitive axiom set is contained in `{propext, Classical.choice, Quot.sound}` — the
> 103: foundational axioms of classical mathematics, nothing more. **0 sorry, 0 project axiom.** By the definition of
> 104: proof in a formal system, all six Clay Millennium problems are proved here. The method that produced the terms
> 105: is not in this file and is not needed to verify it — the kernel already did.

Counter-evidence, from the package itself - premises as ORDINARY BINDERS:
Millennium.lean:324-327:

> 324: theorem P_neq_NP_of_proof_lower_bound (C : ComplexityModel) (q : C.Problem)
> 325:     (hq : C.NPcomplete q) (size : ℕ → ℝ)
> 326:     (hlb : ∀ k : ℕ, ∃ n : ℕ, (n : ℝ) ^ k < size n)
> 327:     (bridge : C.inP q → ∃ k : ℕ, ∀ n : ℕ, size n ≤ (n : ℝ) ^ k) :

and the Riemann final takes `corr` the same way (F07, Millennium.lean:70-73).

## Probe actually run
- Independent reproduction printed the exact claimed footprints (F01), so
  the footprints are right.
- Per-binder analysis (F03-F08) shows unproved premises in four finals. Both
  facts hold simultaneously - the decisive demonstration that "no extra
  axiom -> no smuggled premise" is invalid: hypotheses enter through binder
  TYPES, which #print axioms does not audit.

## Fair analysis
- The technical claim "a PROJECT AXIOM would appear in the footprint" is
  true; the package used none, to its credit.
- The slide from "no project axiom" to "no premise was smuggled" to "all six
  problems are proved" is a non sequitur:
  1. Premises do not appear in axiom footprints; they are binder types
     (counterexample above: corr, hlb, bridge are unproved premises while
     footprints show only the classical trio).
  2. "A kernel-accepted term is a proof of its type" is true - the operative
     question is what the TYPE says. A proof of (P -> Q) with P the
     conjecture is not a proof of Q.
  3. The conditionals become Clay-worthy exactly when terms for corr / hlb /
     bridge / hid are supplied - which is the prize-winning work, absent
     here.
- Fairness: the package does not misreport kernel output; it makes a
  philosophical claim about what kernel facts demonstrate. The claim is
  refutable with the package's own source lines.

## Verdict
REFUTED (as an argument). The footprint evidence is genuine; the inference is
invalid. Unproved premises live in binder types, not axiom lists, and four of
six finals carry exactly such premises.
