# F20 - Division of labor conceded; the verifiable layer is where the certificates must be (rebuttal pass)

## Claim under audit

Rebuttal comments 3 and 4:

    "Lean does not run the quantum computation, and we never claim that it does. … The pipeline is
    therefore mathematical problem → quantum computation of the decisive invariant → discovered
    result → formal certificate → Lean kernel verification of the theorem."

    "The quantum computer is the discovery/computation engine. Lean is the sovereign verifier. … We
    use quantum computation to obtain mathematical information that was previously computationally
    inaccessible, encode the resulting mathematical content into certificates, and ask Lean one
    question only: does this certificate constitute a valid proof of the target proposition?"

## Verbatim quotation (the package's own framing of the same division)

> 147: `bridge`). These premises are the committed spectral certificates of the governed computation, as
> 148: laid out in the paper; the Lean layer proves each implication kernel-checked with 0 `sorry` and 0
> 149: project axiom. `ns_official` and `bsd_official` are definitions of the official Clay statements;

(package README.md:147-149, in the committed audit.py output commentary.)

And the paper (§ "Relation to the paper"): the deciding data are "independent of the private
quantum computation that produced it".

## Probe actually run (2026-09-04)

1. Census (F15): the verifiable layer contains **zero** certificate terms: no `gftqc_*` declaration
   of any kind, no operator, no 300-ordinate table, no rank/order equality, no continuum
   identification.
2. The package's own audit.py classifies the "premises" as unproved binders
   (`hD, corr`, `hc, hid`, `_hL`, `hq, hlb, bridge`) — and the two underscored/free ones (`_hL`,
   never used) are not even load-bearing premises (F06).
3. The paper asserts the certificates are "named, previously-proved theorem[s] in the package"
   (§4) — contradicted by the census of the md5-identical published zip.

## Fair analysis

- **The architecture as described is coherent and is not disputed.** Verified computation has
  exactly this shape (the four-color theorem: a computer produces checkable objects; a kernel —
  Coq — checks them; nobody asks Coq to run the graph program). Conceded without reservation:
  Lean does not need to run quantum computation, and if the pipeline's later stages existed, the
  division of labor would be sound.
- **But the division of labor makes the committed certificate the whole evidentiary burden.** If
  Lean "asks one question only — does this certificate constitute a valid proof?", then the
  certificate must BE in the artifact Lean checks. "Committed" (README:147) is a precise claim:
  the terms should be committed in the package. They are not. What ships instead are conditional
  theorems whose binder types restate the certificates (F04-F08), two defs of open statements
  (F05, F06), and list/monoid arithmetic (F03, F13).
- The kernel-clean footprints are exactly what an empty-certificate layer produces (F17): the
  footprint cannot distinguish "certificates proved" from "certificates never committed" — and the
  census shows the latter.
- Scope guard: the hydrogen-chain/beyond-classical benchmark claims are third-party claims about a
  proprietary computation, outside this audit's evidence base — quarantined per the F14 policy
  (context only, not load-bearing). The Lean-layer verdicts above do not depend on them.

## Verdict

REFUTES HEADLINE (for the published layer). The described pipeline's decisive stage — "encode the
resulting mathematical content into certificates" and commit them for the sovereign verifier — is
exactly the stage that is absent from the published, kernel-checkable artifact.
