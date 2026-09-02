"""Official Clay Millennium statements vs the package's claimed theorems.

Comparison oracle for statement-level audit, from the Clay problem PDFs.
"""
from dataclasses import dataclass


@dataclass(frozen=True)
class ClayStatement:
    name: str
    official_summary: str
    claimed_theorem: str
    claimed_type_summary: str
    gap: str


CLAY_STATEMENTS: dict = {
    "Riemann": ClayStatement(
        "Riemann Hypothesis",
        "Re of every nontrivial zero of riemannZeta is 1/2.",
        "Millennium.riemannHypothesis_of_selfAdjoint_correspondence",
        "IsSelfAdjoint D -> (corr: zeros = 1/2 + I*z, z in spectrum D) -> RiemannHypothesis",
        "Premise corr IS the Hilbert-Polya correspondence - the open problem. "
        "Proving RH given corr is trivial arithmetic. No (D, corr) is constructed.",
    ),
    "Yang-Mills": ClayStatement(
        "Yang-Mills existence and mass gap",
        "4D Yang-Mills exists with Wightman axioms and positive mass gap.",
        "Millennium.yang_mills_gap",
        "forall c m : Real, 0 < c -> m = c -> 0 < m",
        "The theorem is literally substitution 0<c, m=c |- 0<m. No gauge theory, "
        "no Wightman axioms, no existence content. The identification m = c is "
        "an unproved premise.",
    ),
    "Navier-Stokes": ClayStatement(
        "Navier-Stokes existence and smoothness",
        "3D global regularity: smooth solutions never blow up.",
        "Millennium.ns_official",
        "def ns_official (nu) : Prop := the Clay statement itself",
        "A def, not a proof: defining an open conjecture in Lean proves nothing. "
        "The 'theorem navier_stokes' proves only 0 < n+1 over the tower.",
    ),
    "Hodge": ClayStatement(
        "Hodge conjecture",
        "Every rational (p,p) Hodge class on a smooth projective variety is algebraic.",
        "Millennium.hodge_kunneth",
        "conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1]",
        "A list-arithmetic identity (Hodge numbers of CP3 x CP2 by decide). "
        "No varieties, no cohomology, no algebraic cycles in the type.",
    ),
    "BSD": ClayStatement(
        "Birch and Swinnerton-Dyer",
        "Algebraic rank of E(Q) = analytic rank (order of vanishing of L(E,s) at 1).",
        "Millennium.bsd_official",
        "def bsd_official (W) (r) (L) (_hL : L = LSeries) : Prop := finrank = r /\\ order r",
        "A def, not a proof. 'theorem bsd' proves only 0 < n+1 over the tower.",
    ),
    "P-vs-NP": ClayStatement(
        "P versus NP",
        "P = NP or P != NP.",
        "Millennium.P_neq_NP_of_proof_lower_bound",
        "NPcomplete q -> (hlb: superpoly lower bound) -> (bridge: inP -> poly size) -> P_neq_NP C",
        "Both premises are the unresolved content: hlb is a proof-system lower "
        "bound far beyond known results; bridge (proof-complexity -> algorithmic "
        "hardness) has never been achieved. NPcomplete is an uninterpreted "
        "interface field.",
    ),
}
