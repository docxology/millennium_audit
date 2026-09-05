# F17 - A "named, consumed, unproved certificate" in Lean is an axiom — kernel receipt (rebuttal pass)

## Claim under audit

Rebuttal comment on P vs NP:

    "gftqc_bridge in P ≠ NP is not merely an assumed premise. It is explicitly the named universal
    all-algorithm transfer certificate consumed by the closed final theorem."

Paper §4: "Each gftqc_* certificate is a named, previously-proved theorem in the package (discharged
by GFTQC), consumed here into a closed final of the bare official type."

## Verbatim quotation (the footprint the package itself brandishes)

> 36: **No theorem below depends on anything else.** In particular: no `sorryAx` (there is no `sorry`), and no
> 37: project-specific axiom. If any premise were smuggled in as an assumption, it would appear here as an extra
> 38: axiom. It does not. The footprint is the same three (or fewer) that underlie all of mathlib.

(PROOF_CERTIFICATE.md:36-38.)

## Probe actually run (2026-09-04, Lean 4.34.0-rc1, pinned mathlib, exit 0)

Wrote the rebuttal's architecture out exactly in Lean — certificates as NAMED declarations consumed
by a closed final — and printed the footprint:

```lean
axiom gftqc_hlb : ∀ (C : ComplexityModel) (q : C.Problem) (size : ℕ → ℝ) (k : ℕ),
    ∃ n : ℕ, (n : ℝ) ^ k < size n
axiom gftqc_bridge : ∀ (C : ComplexityModel) (q : C.Problem) (size : ℕ → ℝ),
    C.inP q → ∃ k : ℕ, ∀ n : ℕ, size n ≤ (n : ℝ) ^ k
theorem p_neq_np_final : P_neq_NP junkModel :=
  P_neq_NP_of_proof_lower_bound junkModel () trivial (fun _ => 0)
    (gftqc_hlb junkModel () (fun _ => 0))
    (gftqc_bridge junkModel () (fun _ => 0))
#print axioms p_neq_np_final
```

Kernel output:

```
'p_neq_np_final' depends on axioms: [gftqc_bridge, gftqc_hlb, propext, Classical.choice, Quot.sound]
```

The two alternatives for a "named, consumed" certificate are exhaustive:

1. **Named but unproved** (`axiom`): it appears by name in `#print axioms` — the receipt above.
2. **Named and proved**: then the proof term of, e.g., `gftqc_bridge : inP q → polynomial-size
   refutations` (the proof-complexity→algorithm transfer) or `gftqc_corr` (the Hilbert–Pólya
   correspondence) would itself be the Millennium result — the very content absent from the
   package (F07, F08).

There is no third option for a NAMED certificate.

   (A third shape — an anonymous inline term inside a final's proof body — is neither named nor an
   axiom, but it is not what the rebuttal describes ("the NAMED universal all-algorithm transfer
   certificate"), and it would place the full mathematical content inside the package's own files,
   where the census (F15) shows it is absent.) The package's shipped footprints contain no
   `gftqc_*` names and no proofs of them — consistent with F15: the certificates were never
   committed.

## Fair analysis

- This closes the F10 loop using the authors' own naming scheme. F10 established that unproved
  premises enter through binder TYPES, invisible to `#print axioms` — true of the shipped
  conditionals. The rebuttal's architecture goes further: it *names* the premises as
  first-class certificates consumed by closed finals. Under that architecture, PROOF_CERTIFICATE.md's
  own decisive-evidence claim ("if any premise were smuggled in as an assumption, it would appear
  here as an extra axiom") becomes exactly right — and against a package that actually contained
  the consumed gftqc_* terms, the printed footprints would show `gftqc_corr`, `gftqc_hlb`,
  `gftqc_bridge`, `gftqc_ns_global`, `gftqc_hodge_algebraic`, `gftqc_bsd_rank_eq_order` as extra
  axioms unless each were genuinely proved.
- The package's actual footprints (`[propext, Classical.choice, Quot.sound]`) therefore certify the
  absence of the certificates, not the presence of the conclusions. The paper's §4 audit (a)
  ("each footprint ⊆ {propext, Classical.choice, Quot.sound}, with no sorryAx and no project
  axiom") is only consistent with §4's finals if the finals do not exist in the package — which is
  what the census shows.

## Verdict

REFUTES HEADLINE. Under the rebuttal's own description, a consumed unproved certificate is a Lean
axiom and prints in the very axiom report the package presents as decisive; the published package
prints no such names because it contains no such certificates.
