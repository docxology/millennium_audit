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
  decoration only, as described in Methodology).
- Fairness of classification: CONDITIONAL_IMPLICATION vs OFF_TOPIC_THEOREM
  is a judgment call for edge cases; for this package every classification
  is over-determined (e.g. Yang-Mills is both conditional AND its type is
  bare substitution).
- The audit concerns the published archive `MillenniumLean_ClayProof_20260901.zip`.

## Related work

- LeanMillenniumPrizeProblems provides reference formalizations [@leandojo].
- Opera Numerorum provides examples of theorems verified in Lean. [Project source](https://github.com/DavidFox998/opera-numerorum)
- PostQuantum discusses the companion FTQC paper [@postquantum2026].
The verdict relies on the audited package and its theorem types.
