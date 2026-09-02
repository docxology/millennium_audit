# F09 - audit.py "CLOSED" classification: a category error presented as evidence

## Claim under audit
The package's committed audit.py output (README.md, "audit.py output
(committed)") classifies Navier-Stokes and Hodge as CLOSED, and the README
interprets premises as "committed spectral certificates".

## Verbatim quotation (exact bytes)
README.md (audit.py output section), as committed in the package README:

> 121: CLOSED-TERM AUDIT - explicit binders in each final's type (balanced-paren parse)
> 122: 
> 123: [Riemann]  theorem riemannHypothesis_of_selfAdjoint_correspondence
> 124:    -> CONDITIONAL - premises: hD, corr  [data: D]

audit.py:41-43 (classification logic):

> 41:     out, depth, start = [], 0, None
> 42:     for idx, c in enumerate(sig):
> 43:         if c == "(":

audit.py:36-37 (premise heuristic - by binder NAME):

> 36:         j += 1
> 37:     return kind, src[i:j]

## Probe actually run
- Executed the package's audit.py unmodified: reproduced its committed output.
- Re-parsed the same signatures with our independent parser
  (src/lean_parser.py): identical binder lists - the mechanics are correct.
- Checked declaration kinds of the "CLOSED" finals: hodge_kunneth is a
  theorem (off-topic, F03); ns_official and bsd_official are defs (F05, F06).

## Fair analysis
- The balanced-paren parsing is competently written; CONDITIONAL
  classifications are accurate.
- The error is semantic: for a THEOREM, a closed type would mean the
  conclusion stands alone. For a DEF (ns_official, bsd_official),
  binder-closedness is meaningless: a def of an open conjecture has no
  premises because it has no proof at all. Labeling it "CLOSED" invites
  counting it as a settled result; the honest label is "UNPROVED (definition
  of open problem)".
- The premise detector classifies by BINDER NAME (starts with "h", or named
  corr/bridge/step), not semantics: audit.py:36-37. An unproved hypothesis
  named `D`, `L`, or `size` would not be flagged. In
  P_neq_NP_of_proof_lower_bound the superpolynomial bound is `hlb` (flagged)
  while the unproved `size` function is silently counted as "data".
  Name-based premise detection cannot establish that a type is
  unconditionally proved.


## Reinforcement found in red-team pass (2026-09-01)

The package's own `print_axioms.lean` includes the two DEFS in its axiom
report: `#print axioms Millennium.ns_official` and
`#print axioms Millennium.bsd_official` (print_axioms.lean:10-11). Printing
axioms of a def is trivially satisfiable - a def has no proof term at all -
so including them in the "axiom footprint" table extends the F09 category
error from audit.py's CLOSED label to the package's headline evidence
artifact itself. (Source: package/MillenniumLean/print_axioms.lean, read
verbatim in the red-team pass.)

## Verdict
CONFIRMED (misleading). The parser is honest; the CLOSED/CONDITIONAL frame
conflates "no premise binder" with "no unproved premise", and the name
heuristic under-reports premises. Technically accurate lines, misleading
evidential framing.
