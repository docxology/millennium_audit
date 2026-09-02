# Scope, limitations, and related work

## What this audit is

A statement-level audit of one public artifact: does any type in the package
settle a Clay Millennium Problem? Every verdict is re-derivable from the
cited file:line anchors.

## What this audit is not

- It does not adjudicate the companion paper's quantum-computing claims;
  finding F14 records the public record as context only.
- It does not evaluate the proprietary "governed computation" layer, which
  the package itself says is not needed to verify the theorems - correctly,
  because there is nothing substantive in the certificate layer to verify.
- It does not claim the package's kernel facts are false; F01 confirms them.

## Limitations

- The mathlib clone was shallow at the pinned revision (provenance
  decoration only; see Section 2).
- Fairness of classification: CONDITIONAL_IMPLICATION vs OFF_TOPIC_THEOREM
  is a judgment call for edge cases; for this package every classification
  is over-determined (e.g. Yang-Mills is both conditional AND its type is
  bare substitution).
- We audited the 20260901 zip as published; a newer revision could differ
  (none was available on Zenodo as of the audit date).

## Related work

- lean-dojo/LeanMillenniumPrizeProblems - reference formalizations of all
  seven problems, marked Open.
- DavidFox998/opera-numerorum - 664 verified Lean "bricks" with an explicit
  honesty statement that no Clay problem is solved.
- postquantum.com's detailed critique of the companion FTQC paper.
These agree with, but are not load-bearing for, the present verdict.
