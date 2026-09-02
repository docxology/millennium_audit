# F14 - External context: the companion paper's public verification record

## Purpose
The Lean package is the "public, independently-verifiable certificate layer"
of the AIX Global paper. This finding records the surrounding public record
and the package's isolation argument. Context only - the audit verdict rests
on F01-F13 alone.

## Verbatim quotation (exact bytes)
README.md ("Relation to the paper" section):

> 158: computation that produced the deciding spectral data is a separate, proprietary layer and is **not
> 159: required to verify these theorems**: the Lean kernel checks the committed terms, and how they were
> 160: produced is irrelevant to whether they type-check.
> 161: 
> 162: © 2026 AIX Global Innovations, Inc. All rights reserved. This work is distributed by the authors
> 163: under a non-exclusive license permitting deposit on academic preprint repositories. No Creative

## Probe actually run
Web retrieval (2026-09-01). Key documented findings:

1. postquantum.com, "AIX Global Innovations FTQC Claim Doesn't Survive Its
   Paper" (postquantum.com/industry-news/aix-global-ftqc-claim-analysis/):
   - the paper's own sentence: "Seed IQ governance acts as an operational
     substitute for code distance" - at code distance d=1, which corrects
     zero errors by definition;
   - surface-code qubit counts misstated (13/41 vs the correct 17/49 for
     d=3/5);
   - per-shot post-selection documented in the paper's Section 13.9,
     contradicting the summary "Data rejection / post-selection: None";
   - the twelve-decimal cross-chip agreement self-described in the paper as
     "the engineered signature of Seed IQ's admissibility-and-projection
     contract" - engineered convergence offered as discovery;
   - founder response to technical objections: "I guarantee you don't
     because you've never seen anything like this."
2. lean-dojo/LeanMillenniumPrizeProblems: all seven problems formally stated,
   marked Open - the reference formalization effort.
3. DavidFox998/opera-numerorum Honesty Statement: "No Clay Millennium Prize
   problem has been solved by this project" - from an active Lean program
   with 664 verified bricks.

## Fair analysis
- The package's sentence "how they were produced is irrelevant to whether
  they type-check" is TRUE for type-checking - and precisely the problem: a
  certificate layer whose theorems are conditionals and tautologies could be
  produced by any means. The quantum layer is doubly unverifiable:
  proprietary, and not needed for the formal layer to check (nothing
  substantive to verify).
- The "committed spectral certificates" that the conditionals' premises
  would need (corr, hid, hlb, bridge terms) appear NOWHERE in the package as
  machine-readable artifacts. Verified: the zip holds 10 files (plus one
directory entry - 11 unzip entries total) - the .lean sources, two
markdowns, audit.py, and build config. A committed
  certificate consumable by Lean must be a term; none ships.
- Fairness: we do not adjudicate the FTQC physics claims; F14 records
  third-party analysis only. The Lean layer is fully assessed in F01-F13
  without any reference to the FTQC dispute.

## Verdict
CONFIRMED (third-party record, supporting context). The external record is
adversarial and detailed; the isolation argument is formally correct and
practically empty because the certificate layer's own types do not carry the
prize-winning content.
