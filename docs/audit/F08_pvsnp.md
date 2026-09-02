# F08 - P vs NP: diagonalization from premises that restate the conjecture

## Claim under audit
README.md table row: "P vs NP -> Millennium.P_neq_NP_of_proof_lower_bound".
WHY_THIS_IS_PROOF.md section 6: "The transfer to all algorithms is closed in
the companion computed corpus (SQ dimension + SOS + natural-proofs evasion +
LPN). P != NP."

## Verbatim quotation
Millennium.lean:324-333 (the named final, complete):

> 324: theorem P_neq_NP_of_proof_lower_bound (C : ComplexityModel) (q : C.Problem)
> 325:     (hq : C.NPcomplete q) (size : ℕ → ℝ)
> 326:     (hlb : ∀ k : ℕ, ∃ n : ℕ, (n : ℝ) ^ k < size n)
> 327:     (bridge : C.inP q → ∃ k : ℕ, ∀ n : ℕ, size n ≤ (n : ℝ) ^ k) :
> 328:     P_neq_NP C := by
> 329:   refine ⟨q, hq, ?_⟩
> 330:   intro hP
> 331:   obtain ⟨k, hk⟩ := bridge hP
> 332:   obtain ⟨n, hn⟩ := hlb k
> 333:   exact absurd (hk n) (not_le.mpr hn)

Millennium.lean:305-315 (the interface and target):

> 305: /-- P vs NP interface (mathlib has no complexity theory): a model carrying P, NP and
> 306:     NP-complete predicates over a problem type. `P_neq_NP` is the real Clay statement — some
> 307:     NP-complete problem is NOT in P. Stated against this interface, NOT rfl-faked. -/
> 308: structure ComplexityModel where
> 309:   Problem : Type
> 310:   inP : Problem → Prop
> 311:   inNP : Problem → Prop
> 312:   NPcomplete : Problem → Prop
> 313:   complete_in_NP : ∀ q, NPcomplete q → inNP q
> 314: 
> 315: def P_neq_NP (C : ComplexityModel) : Prop := ∃ q, C.NPcomplete q ∧ ¬ C.inP q

Millennium.lean:294-303 (the "superpolynomial" support, complete):

> 294: /-- Size–width ⟹ SUPERPOLYNOMIAL size: for every polynomial degree k, eventually xᵏ < eˣ. The 2^Ω(n)
> 295:     refutation lower bound beats every polynomial — no polynomial-size refutation exists in the system. -/
> 296: theorem pvsnp_size_superpoly (k : ℕ) : ∀ᶠ x : ℝ in Filter.atTop, x ^ k < Real.exp x := by
> 297:   have h := Real.tendsto_pow_mul_exp_neg_atTop_nhds_zero k
> 298:   have h1 : ∀ᶠ x : ℝ in Filter.atTop, x ^ k * Real.exp (-x) < 1 :=
> 299:     h.eventually_lt_const (by norm_num)
> 300:   filter_upwards [h1] with x hx
> 301:   have hexp : (0:ℝ) < Real.exp x := Real.exp_pos x
> 302:   rw [Real.exp_neg, ← div_eq_mul_inv] at hx
> 303:   exact (div_lt_one hexp).mp hx

## Probe actually run
- Parsed binders: premises `hq`, `hlb`, `bridge` (CONDITIONAL_IMPLICATION in
  ../../data/audit_report.json; matches the package's own audit.py output).
- Verified the proof is 4 tactic lines of contradiction between hlb and bridge
  (lines 329-333).
- Grep: `bridge` occurs only as this hypothesis; no theorem in the package
  instantiates or proves bridge for any model.

## Fair analysis
- The 4-line contradiction is correct and kernel-checked: a polynomial size
  cap (bridge) contradicts a superpolynomial lower bound (hlb).
- But both premises ARE the problem:
  (hlb) asserts an UNCONDITIONAL superpolynomial lower bound on refutation
  size for some proof system. Known results (Ben-Sasson-Wigderson width,
  Grigoriev/Schoenebeck SOS lifts) give exponential size for resolution and
  degree bounds for SOS on specific families - genuinely known, and far
  weaker than an unconditional bound for a system capturing all of P, which
  is the open frontier. The package's `pvsnp_size_superpoly` (lines 296-303)
  proves only `x^k < e^x` eventually - real calculus, zero proof-complexity
  content.
  (bridge) asserts the transfer "q in P -> polynomial-size refutations" -
  the proof-complexity-to-algorithm bridge never constructed in the
  literature; assumed here as a binder.
- The ComplexityModel interface makes `NPcomplete` an uninterpreted field
  (lines 308-313): no Turing machine model, no verifier, no reduction
  closure. Even the internal target `P_neq_NP C` (line 315) is weaker than
  the real statement.
- The appeal to "the companion computed corpus" points to a proprietary
  artifact outside the verifiable layer; within the package, bridge is never
  discharged.

## Verdict
REFUTES HEADLINE. Correct kernel-checked diagonalization whose nontrivial
premises are beyond current knowledge (hlb, unconditionally) and never
achieved (bridge). The conjecture is assumed, then "derived".
