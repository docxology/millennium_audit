# F18 - The ComplexityModel interface is junk-instantiable: "P≠NP, 0 axioms" in three lines (rebuttal pass)

## Claim under audit

Rebuttal comment: "For P ≠ NP, both gftqc_hlb and gftqc_bridge [are] consumed by
p_neq_np_final : P_neq_NP StandardComplexityModel." Package docstring: "`P_neq_NP` is the real Clay
statement — some NP-complete problem is NOT in P. Stated against this interface, NOT rfl-faked."

## Verbatim quotation

> 305: /-- P vs NP interface (mathlib has no complexity theory): a model carrying P, NP and
> 306:     NP-complete predicates over a problem type. `P_neq_NP` is the real Clay statement — some
> 307:     NP-complete problem is NOT in P. Stated against this interface, NOT rfl-faked. -/
> 308: structure ComplexityModel where
> 309:   Problem : Type
> 310:   inP : Problem → Prop
> 311:   inNP : Problem → Prop
> 312:   NPcomplete : Problem → Prop
> 313:   complete_in_NP : ∀ q, NPcomplete q → inNP q
> 315: def P_neq_NP (C : ComplexityModel) : Prop := ∃ q, C.NPcomplete q ∧ ¬ C.inP q

(Millennium.lean:305-315.)

## Probe actually run (2026-09-04, exit 0)

A junk model satisfying the interface exactly, and the target proved for it:

```lean
def junkModel : ComplexityModel where
  Problem := Unit
  inP := fun _ => False
  inNP := fun _ => True
  NPcomplete := fun _ => True
  complete_in_NP := fun _ _ => trivial
theorem junk_p_neq_np : P_neq_NP junkModel := ⟨(), trivial, fun h => h⟩
#print axioms junk_p_neq_np
```

Kernel output:

```
'junk_p_neq_np' does not depend on any axioms
```

## Fair analysis

- Every field except `complete_in_NP` is unconstrained: no machine model, no verifier, no
  reduction closure, no time bound. `inP`/`inNP`/`NPcomplete` are arbitrary predicates on an
  arbitrary type, so `P_neq_NP C` is a schema whose truth depends entirely on the chosen model —
  here it is a theorem about `Unit` (F08 already noted the interface is uninterpreted; the probe
  makes it concrete and kernel-checked).
- Consequently the docstring's "the real Clay statement" (line 306) is wrong as stated: the real
  Clay statement fixes the model of computation. Recovering it requires interpreting
  `ComplexityModel` with Turing-machine semantics — an interpretation layer mathlib does not have
  and the package does not ship. The paper's `StandardComplexityModel` (absent, F15/F16) would
  have to construct exactly that semantics; no such construction exists in the deposit.
- Connection to F17: whether the premises arrive as binders (`hlb`, `bridge`) or as named axioms
  (`gftqc_hlb`, `gftqc_bridge`), the consumed object for the junk model is equally junk — the
  interface cannot confer Clay content on any instantiation.

## Verdict

REFUTES HEADLINE. The package's P-vs-NP target is a schema provable for junk models with a
zero-axiom footprint; without a semantic interpretation of the model, no instantiation of it —
including the absent `StandardComplexityModel` — is the Clay statement.
