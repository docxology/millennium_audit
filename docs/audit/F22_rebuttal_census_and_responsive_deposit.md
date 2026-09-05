# F22 - Rebuttal-vs-package census and the requirements on a responsive deposit (rebuttal pass)

## Claim under audit

Rebuttal comment 1, per-problem: RH — gftqc_corr "tantam[ount]ed into" riemann_final; Yang-Mills —
"the continuum identification and positive gap certificate are consumed"; Navier-Stokes —
"gftqc_ns_global closes the full ns_official target"; Hodge — "the universal algebraicity
certificate closes OfficialHodgeConjecture"; BSD — "the rank/order certificate closes
OfficialBSDConjecture"; P vs NP — "both gftqc_hlb and gftqc_bridge [are] consumed by
p_neq_np_final."

## Census probe actually run (2026-09-04; grep over the md5-pinned package; Lean probe exit 0)

| Problem | Rebuttal-cited certificate | In published package? | Nearest shipped object (file:line) |
|---|---|---|---|
| Riemann | `gftqc_corr` (+ `gftqc_operator[_selfAdjoint]`) | ABSENT (0 hits) | binder `corr`/`hD`, conditional (Millennium.lean:70-73) |
| Yang-Mills | continuum identification + positive-gap certificate | ABSENT (0 hits; nearest are `ym_twisted_gap_uniform` free-field bound and `(2π/3)² > 0`) | substitution `yang_mills_gap` (:84) |
| Navier-Stokes | `gftqc_ns_global` (global existence) | ABSENT | def `ns_official` (:254) — unproved (F05) |
| Hodge | universal algebraicity certificate (paper Thm 10.7) | ABSENT | list identity `hodge_kunneth` (:45) (F03) |
| BSD | rank/order certificate | ABSENT | def `bsd_official` (:209) with unused `_hL` (F06) |
| P vs NP | `gftqc_hlb`, `gftqc_bridge` | ABSENT | binders `hlb`, `bridge` (:326-327) (F08) |

Kernel probes backing the table: junk-model `P≠NP` zero-axiom (F18); consumed named certificates
print as axioms (F17); junk tower closes any declared target (F19); the §4 block needs 22
undeclared identifiers (F16). Naming nit: the paper itself uses two names for the Hodge
certificate — `gftqc_hodge_algebraic` in the §4 block, `gftqc_hodge` in §10.2D; neither ships.
Package-vs-paper binder nit: the paper's §11 renders the BSD L-series premise as `hL`, the
package declares it `_hL` (underscored, never used).

## What a responsive deposit must contain (items 1-3 kernel-checkable; 4-5 by inspection/build)

1. `Millennium.lean` (or a revision) defining the six `*_final` theorems with exactly the Section-4
   signatures, compiling against the pinned toolchain (`leanprover/lean4:v4.34.0-rc1`, mathlib
   d0be1efe…).
2. The `gftqc_*` certificates as real declarations — proved (then their proofs are the work under
   test and must be reviewed), or `axiom`s (then they print in `#print axioms`, per F17, and
   PROOF_CERTIFICATE.md's own criterion flags them).
3. `StandardComplexityModel` with an actual semantic interpretation of `inP`/`inNP`/`NPcomplete`
   (machine model), or an explicit statement that it is an uninterpreted schema (per F18 it cannot
   then be the Clay statement).
4. An `OfficialHodgeConjecture` with real content — mathlib at the pinned revision has no Chow
   group/algebraic-cycles API to anchor one (F16 probe), so this would itself be new formalization
   work to review.
5. Package README/PROOF_CERTIFICATE/audit.py updated to describe the declarations that actually
   exist (the current committed audit.py output already contradicts the paper's §4 description).

## Fair analysis

- The checklist is deliberately falsifiable: items 1-3 are kernel-checkable properties of the
  deposit; items 4-5 are verifiable by inspection/build. If a revised package satisfies item 1 with
  proved certificates, this audit's headline verdict gets re-run against the new artifact and
  updated.
- Until then, the published record is: conditional theorems (F04, F07, F08), definitions of open
  statements (F05, F06), a trivial invariant (F02), genuine small theorems without Clay content
  (F13), and a paper quoting Lean that the package does not contain (F15, F16).

## Verdict

REFUTES HEADLINE (as of the md5-pinned deposit). Every certificate the rebuttal says is "consumed"
is absent from the published package; the finding converts to CONFIRMED-if-revised upon a deposit
that actually contains the Section-4 development.
