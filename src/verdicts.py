"""Top-level audit verdict combining all lenses, with exact evidence lines."""

# The smoking gun: Tower.lean line 11 - the "universalization tower" invariant.
TOWER_INV_QUOTE = "def declInv (n : Nat) : Prop := 0 < n + 1"

# The "proved" Hodge/BSD/Navier-Stokes theorems all reduce to this:
TOWER_UNIVERSAL_QUOTE = (
    "theorem universal (step : ∀ n, declInv n → declInv (n + 1)) : ∀ n, declInv n"
)

VERDICTS = {
    "headline": (
        "NONE of the six Clay Millennium Problems is resolved by this package. "
        "The Lean kernel checks that trivial implications and list identities "
        "type-check; the entire mathematical content of each problem sits in "
        "unproved premise binders, in a def of the open statement, or is "
        "replaced by an unrelated toy theorem."
    ),
    "tower_smoking_gun": (
        "Tower.lean:11 defines declInv n := 0 < n + 1. The theorems named "
        "'hodge', 'bsd', 'navier_stokes', 'poincare_control' all equal "
        "Tower.universal applied to this: they prove only 'for all naturals n, "
        "0 < n + 1' - true by Nat.succ_pos, zero mathematical content. The "
        "package's own PROOF_CERTIFICATE.md prints 'Tower.poincare_control "
        "does not depend on any axioms' as evidence - a tautology is "
        "axiom-free by nature."
    ),
    "audit_py_confession": (
        "The package's own audit.py output classifies Riemann, Yang-Mills, BSD "
        "and P-vs-NP finals as 'CONDITIONAL - premises: ...'. A conditional "
        "statement with unproved premises is not a proof of its conclusion."
    ),
    "kernel_facts": (
        "The kernel-level claims (builds clean, 0 sorry, 0 project axiom, "
        "axioms in {propext, Classical.choice, Quot.sound}) are likely TRUE as "
        "stated - and irrelevant. Axiom-freedom of an implication with unproved "
        "premises, or of '0 < n+1', is expected and proves nothing about the "
        "Clay problems."
    ),
    "external_context": (
        "The companion paper's FTQC claims were independently demolished "
        "(postquantum.com: code distance 1 = zero error correction; hidden "
        "per-shot post-selection contradicting 'Data rejection: None'; the "
        "12-decimal cross-chip identity self-described as an 'engineered "
        "signature'). The honest Lean formalization community (lean-dojo "
        "LeanMillenniumPrizeProblems, opera-numerorum honesty statement: 'No "
        "Clay Millennium Prize problem has been solved by this project') marks "
        "all six problems OPEN."
    ),
    "epistemic_status": (
        "Verified by direct reading of all 11 package files (verbatim, this "
        "session) plus real file hashes; Lean kernel build/axiom reproduction "
        "recorded separately with toolchain v4.34.0-rc1 per lean-toolchain. "
        "Kernel reproduction confirms build hygiene only - it cannot and does "
        "not rescue conditional premises. Statement-level gap analysis "
        "re-derivable from Millennium.lean lines 70-84, 88-93, 102-114, 209-211, "
        "254-264, 324-333 and Tower.lean lines 11-26."
    ),
}
