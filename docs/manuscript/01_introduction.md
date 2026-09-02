# Introduction

## The claim

On 2026-09-01, AIX Global, Inc. published MillenniumLean - "the six remaining
Clay Millennium Problems, machine-checked in Lean 4" - as the public,
independently-verifiable certificate layer of its paper "Demonstrating Quantum
Value by Solving the Six Remaining Clay Millennium Problems" (Holt &
Ovseyenko, Zenodo DOI 10.5281/zenodo.22179463). The package README states the
six "final theorems" by name, asserts "0 sorry, 0 project axiom", and offers
`#print axioms` output as the decisive evidence. A companion document,
WHY_THIS_IS_PROOF.md, opens: "This is done. State it as done."

An extraordinary claim requires extraordinary evidence. The certificate layer
is public; this audit holds it to the standard it itself invokes: a Lean term
the kernel accepts is a proof **of its type** - so the entire question is
what the types say.

## Scope and fairness posture

Three commitments govern everything below.

1. **No kernel fact is disputed.** We reproduce the build and axiom report
   independently (Section 2; finding F01) and they match the package
   byte-for-byte.
2. **Every refutation is quote-anchored.** Each of the fourteen findings
   (docs/audit/F01-F14) quotes the package's own source lines, with file:line
   verified character-against the extracted tree by a script (259/259 quoted
   lines verify byte-exact).
3. **Genuine content is credited.** Finding F13 itemizes the package's real
   theorems and faithful formalizations; the verdict rests on what is absent,
   not on denying what is present.

## Reader's guide

Section 2 records the reproduction; Section 3 the audit method; Section 4 the
per-problem results; Section 5 the cross-cutting findings; Section 6 the
external record (context only); Section 7 reproducibility of the audit
itself; Section 8 scope limits. The Epistemic Status paragraph (Section 9)
states exactly what was run and what remains unverified.
