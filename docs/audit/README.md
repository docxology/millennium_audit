# audit/

Twenty-two itemized findings, one file per finding, plus the index.

| File | Verdict (short) |
|------|-----------------|
| [`00_INDEX.md`](00_INDEX.md) | Index, verdict table, self-audit receipt, fairness statement |
| [`F01_kernel_build_receipt.md`](F01_kernel_build_receipt.md) | Kernel claims CONFIRMED and independently reproduced - evidentially void |
| [`F02_tower_invariant.md`](F02_tower_invariant.md) | Tower proves only `0 < n + 1` - REFUTES HEADLINE |
| [`F03_hodge.md`](F03_hodge.md) | List arithmetic, no Hodge content - REFUTES |
| [`F04_yang_mills.md`](F04_yang_mills.md) | Substitution, no gauge theory - REFUTES |
| [`F05_navier_stokes.md`](F05_navier_stokes.md) | Def of the open problem - REFUTES |
| [`F06_bsd.md`](F06_bsd.md) | Def of the conjecture - REFUTES |
| [`F07_riemann.md`](F07_riemann.md) | Conditional on the open problem - REFUTES |
| [`F08_pvsnp.md`](F08_pvsnp.md) | Premises restate the conjecture - REFUTES |
| [`F09_audit_py_category_error.md`](F09_audit_py_category_error.md) | Package's own audit misleads - CONFIRMED (misleading) |
| [`F10_axiom_footprint_rhetoric.md`](F10_axiom_footprint_rhetoric.md) | Premises-as-axioms inference invalid - REFUTED (as argument) |
| [`F11_poincare_control.md`](F11_poincare_control.md) | Tautological control validates nothing - SELF-DEFEATING |
| [`F12_klein_theta_offtopic.md`](F12_klein_theta_offtopic.md) | True but unrelated theorems - OFF_TOPIC |
| [`F13_genuine_content_fair_credit.md`](F13_genuine_content_fair_credit.md) | Real content itemized - CONFIRMED (fair credit) |
| [`F14_external_context.md`](F14_external_context.md) | Public record - CONFIRMED (context only) |
| [`F15_published_package_has_no_finals.md`](F15_published_package_has_no_finals.md) | Rebuttal pass: paper §4 finals absent from the published package - REFUTES |
| [`F16_paper_lean_block_cannot_typecheck.md`](F16_paper_lean_block_cannot_typecheck.md) | Paper §4 Lean block needs 22 undeclared identifiers - REFUTES |
| [`F17_certificates_are_axioms_kernel_receipt.md`](F17_certificates_are_axioms_kernel_receipt.md) | Consumed named certificates print as axioms (kernel receipt) - REFUTES |
| [`F18_complexity_model_junk_instantiation.md`](F18_complexity_model_junk_instantiation.md) | Junk model: closed zero-axiom P≠NP - REFUTES |
| [`F19_tower_closes_proves_anything.md`](F19_tower_closes_proves_anything.md) | PROMOTE mechanism proves any declared target - CONFIRMED (content-free) |
| [`F20_division_of_labor_missing_certificates.md`](F20_division_of_labor_missing_certificates.md) | Architecture conceded; certificates absent from verifiable layer - REFUTES |
| [`F21_hilbert_polya_certificate_status.md`](F21_hilbert_polya_certificate_status.md) | `gftqc_corr` is the unproved Hilbert–Pólya binder - REFUTES |
| [`F22_rebuttal_census_and_responsive_deposit.md`](F22_rebuttal_census_and_responsive_deposit.md) | Per-problem census + falsifiable checklist for a responsive deposit - REFUTES (as of pinned md5) |

Every quotation is line-anchored; 259/259 verified byte-exact against the
package (see 00_INDEX.md self-audit receipt). The rebuttal pass (F15-F22,
2026-09-04) adds kernel exit-0 Lean probes and a md5 artifact-identity pin;
its paper quotations are from the published Zenodo PDF text (00_INDEX.md
rebuttal-pass receipt).
