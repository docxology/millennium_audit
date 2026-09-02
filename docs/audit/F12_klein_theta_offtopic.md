# F12 - Klein ZMod-12 and theta-gap theorems: true, kernel-checked, off-topic

## Claim under audit
Millennium.lean introduces "Phase C: L36 finite kernel" and the "contextuality
gap" as part of the P vs NP / strict-identity narrative.

## Verbatim quotation (exact bytes)
Millennium.lean:266-273 (Phase C narrative and the two Klein theorems):

> 266: /- ── Phase C: L36 finite kernel, FINISHED by exact `ZMod 12` arithmetic (no floating point) ──
> 267:    The strict-identity : frame-trivial ratio on the Klein moduli is exactly 1:2 because the Klein
> 268:    relation b·a·b⁻¹ = a⁻¹ forces the central ℤ/12 phase p of the a-generator to satisfy 2p = 0, whose
> 269:    solutions in `ZMod 12` are exactly {0, 6}. Both proofs are complete (`decide`). -/
> 270: theorem klein_central_involutions :
> 271:     (Finset.univ.filter (fun p : ZMod 12 => 2 * p = 0)) = {0, 6} := by decide
> 272: theorem klein_frame_strict_ratio_two :
> 273:     (Finset.univ.filter (fun p : ZMod 12 => 2 * p = 0)).card = 2 := by decide

Millennium.lean:282-292 (contextuality-gap narrative and theorem):

> 282: /-- Intensive boundary expansion ⟹ a positive LINEAR width lower bound: δ>0, n>0 give width δ·n>0,
> 283:     scale-invariant (not vanishing under refinement). The Ben-Sasson–Wigderson width core. -/
> 284: theorem pvsnp_width_linear (δ n : ℝ) (hδ : 0 < δ) (hn : 0 < n) : 0 < δ * n := mul_pos hδ hn
> 285: 
> 286: /-- Contextuality gap, STRICT: on the 5-cycle α(C₅)=2 < ϑ(C₅)=√5. The poly-time Lovász theta
> 287:     relaxation strictly exceeds the true independence number, so the integrality gap (contextuality) is
> 288:     not identically zero — a computed obstruction to closing P=NP by convex relaxation. -/
> 289: theorem pvsnp_theta_gap_strict : (2 : ℝ) < Real.sqrt 5 := by
> 290:   have h : (2:ℝ) = Real.sqrt 4 := by
> 291:     rw [show (4:ℝ) = 2^2 by norm_num, Real.sqrt_sq (by norm_num)]
> 292:   rw [h]; exact Real.sqrt_lt_sqrt (by norm_num) (by norm_num)

## Probe actually run
- Verified the exact lines (this session).
- Independent axiom report: klein_frame_strict_ratio_two and
  pvsnp_theta_gap_strict depend only on [propext, Classical.choice,
  Quot.sound] or fewer - consistent with the package certificate.

## Fair analysis
- All three are TRUE and kernel-checked: `decide` proofs of finite facts and
  the `2 < sqrt 5` inequality admit no doubt.
- Their connection to the Clay problems:
  - Klein theorems: the 2-torsion of Z/12 is {0, 6} - a one-line
    computation. The "frame-trivial ratio 1:2" narrative lives entirely in
    comments; no monodromy, moduli space, or frame object appears in any
    type.
  - pvsnp_theta_gap_strict: alpha(C5) = 2 and theta(C5) = sqrt 5 are
    well-known, but the theorem only proves `2 < Real.sqrt 5` as REAL
    NUMBERS. The independence number alpha, the Lovasz theta function, and
    the integrality gap never appear as formal objects. As an argument
    against "closing P=NP by convex relaxation" it is a gesture, not a
    theorem - and irrelevant to P != NP in any case.
- Fairness: these are exactly the real-but-toy lemmas that make the corpus
  look substantial. The package has 41 declarations; each is credited as
  true in F13 while none carries Clay content.

## Verdict
OFF_TOPIC (real but unrelated). Kernel-validated finite arithmetic and a
real-number inequality; the Clay-relevant objects are absent from all types.
