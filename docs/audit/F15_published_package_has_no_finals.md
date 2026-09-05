# F15 - The published package contains none of the six `*_final` theorems (rebuttal pass)

## Claim under audit

LinkedIn rebuttal comments (D. Ovseyenko, 2026-09-04, replying to this audit):

    "Section 4 gives the actual closed final theorems: riemann_final : RiemannHypothesis,
    yang_mills_final : OfficialYangMillsStatement, navier_stokes_final,
    hodge_final : OfficialHodgeConjecture, bsd_final : OfficialBSDConjecture, and
    p_neq_np_final : P_neq_NP StandardComplexityModel. These have no remaining bridge hypotheses."

and: "the next check is straightforward: inspect the six *_final declarations and their dependency
trees, rather than treating Tower.universal as their endpoint."

## Verbatim quotation (the artifact the rebuttal points at)

Paper v1.0 (Zenodo DOI 10.5281/zenodo.22179463, "The six closed final theorems", pp. 14-15;
PDF text extraction, typographic ligatures normalized):

```
To leave no ambiguity about what the public Lean 4 package contains, we state up front the closed
final theorem for each Clay problem. Each is a kernel-checked term of the bare official type—no
remaining hypothesis—obtained by applying the displayed core theorem to named, previously-proved
GFTQC certificates. The central arguments (corr, step, hlb, bridge) are consumed, not assumed.

#check riemann_final
#check yang_mills_final
#check navier_stokes_final
#check hodge_final
#check bsd_final
#check p_neq_np_final
```

```
Each gftqc_* certificate is a named, previously-proved theorem in the package (discharged by
GFTQC), consumed here into a closed final of the bare official type.
```

## Probe actually run (2026-09-04)

1. **Artifact identity.** The audited zip's md5 is `99df5b03a4798bfe543b03f525face13`; the Zenodo
   record 22226553 (v2, published 2026-09-01 — the paper's own "supplemental computational notebook
   with Lean Proofs" link) lists its file `MillenniumLean_ClayProof_20260901.zip` with the identical
   md5. The audited artifact IS the currently published one. Red-team re-run: ALL TEN file members
   of the zip are SHA-256-identical to `package/MillenniumLean/`. The concept's earlier version
   (record 22225697, same zip name, md5 `c20731d652568a954afe1c66b45df1b3`, 21450 B) is a different
   artifact; this audit pins v2.
2. **Identifier census.** `grep -c gftqc` over all package `.lean` and `.md`: **0** everywhere.
   `grep _final`: **0** hits. `grep StandardComplexityModel`: **0** hits.
3. **Full declaration census** (53 headers, 41 declarations, `Millennium.lean` + `Tower.lean`):
   no declaration of any kind is named `*_final`, `gftqc_*`, `StandardComplexityModel`,
   `OfficialYangMillsStatement`, `OfficialHodgeConjecture`, or `OfficialBSDConjecture`. The only
   `Official*` string in the package is the structure field `OfficialTarget : Prop`
   (Millennium.lean:360). No `axiom` declaration exists.
4. **The package's own endpoint list** disagrees with the paper's:

   | Paper §4 "#check" | Package `print_axioms.lean` actually prints |
   |---|---|
   | `riemann_final` | `Millennium.riemannHypothesis_of_selfAdjoint_correspondence` (conditional, F07) |
   | `yang_mills_final : OfficialYangMillsStatement` | `Millennium.yang_mills_gap` (substitution, F04) |
   | `navier_stokes_final` | `Millennium.ns_official` — a **def**, not a theorem (F05) |
   | `hodge_final : OfficialHodgeConjecture` | `Millennium.hodge_kunneth` (list identity, F03) |
   | `bsd_final : OfficialBSDConjecture` | `Millennium.bsd_official` — a **def** (F06) |
   | `p_neq_np_final : P_neq_NP StandardComplexityModel` | `Millennium.P_neq_NP_of_proof_lower_bound` (conditional, F08) |

5. The paper's audit description also contradicts the package's own committed audit output:
   paper §4: "(b) Closed-term audit: each *_final has the bare official type (§4) with no remaining
   hypothesis" — while the package's committed `audit.py` output (package README:121-150) classifies
   the six endpoints as CONDITIONAL (premises `hD, corr`, `hc, hid`, `_hL`, `hq, hlb, bridge`) with
   `ns_official`/`bsd_official` as defs.

## Fair analysis

- The rebuttal's quotations of Section 4 are accurate — the paper does contain that block. The
  failure is the referent: "Each gftqc_* certificate is a named, previously-proved theorem **in the
  package**" is false of the only published, checkable package, whose final-theorem table (README:7-14)
  names exactly the six conditional/def endpoints this audit already adjudicated (F01-F08).
- A reader following the rebuttal's own instruction — "inspect the six *_final declarations and
  their dependency trees" — finds no such declarations in the published, runnable artifact. The
  dependency trees that DO exist terminate in unproved premise binders (F04-F08) and the `0 < n + 1`
  tower (F02).
- Nothing here disputes any kernel output of the package (fairness commitment preserved); the
  dispute is over what the published artifact contains.

## Verdict

REFUTES HEADLINE. The six closed `*_final` theorems exist only as quoted text in the paper; the
published, kernel-checkable package (md5-pinned) contains none of them, and the package's own
endpoint list and audit output say so.
