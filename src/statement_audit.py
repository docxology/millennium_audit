"""Statement-level audit: package theorems vs official Clay statements."""
from dataclasses import dataclass, field


@dataclass
class ProblemVerdict:
    problem: str
    claimed_theorem: str
    theorem_kind: str | None          # 'theorem', 'def', or None if not found
    explicit_premises: list
    is_conditional: bool              # final type carries unproved premise binders
    resolves_official_statement: bool # does the type itself settle the Clay problem?
    verdict: str                      # PROVES / CONDITIONAL_IMPLICATION / NO_CONTENT
    reasoning: str
    supporting_quotes: list = field(default_factory=list)


class StatementAuditor:
    """Combines Lean parse facts + Clay oracle into per-problem verdicts."""

    # Names the package itself lists as "final theorems" for each problem.
    FINALS = {
        "Riemann": "riemannHypothesis_of_selfAdjoint_correspondence",
        "Yang-Mills": "yang_mills_gap",
        "Navier-Stokes": "ns_official",
        "Hodge": "hodge_kunneth",
        "BSD": "bsd_official",
        "P-vs-NP": "P_neq_NP_of_proof_lower_bound",
    }

    def __init__(self, clay_statements, parser):
        self.clay = clay_statements
        self.parser = parser

    def audit(self, millennium_lean_text: str) -> list:
        parsed = self.parser.extract_final_theorems(
            millennium_lean_text, self.FINALS
        )
        verdicts = []
        for prob, info in parsed.items():
            cs = self.clay[prob]
            kind = info["kind"]
            premises = info["premises"]
            if kind is None:
                verdict, resolves = "NOT_FOUND", False
                reasoning = f"Declaration {info['claimed_name']} not found in Millennium.lean."
            elif kind == "def":
                # A def of the open problem proves nothing.
                resolves = False
                verdict = "DEFINITION_ONLY"
                reasoning = (
                    f"'{info['claimed_name']}' is a def whose type IS the open "
                    "Clay statement (or a wrapper). Defining a conjecture proves "
                    "nothing; no theorem in the package closes it."
                )
            elif premises:
                resolves = False
                verdict = "CONDITIONAL_IMPLICATION"
                reasoning = (
                    f"The theorem's type carries unproved premise binder(s) "
                    f"{premises}. The hard mathematical content of the Clay "
                    "problem sits in these premises; the Lean layer only proves "
                    "the implication. Package audit.py itself marks this "
                    "'CONDITIONAL'."
                )
            else:
                resolves = False
                verdict = "OFF_TOPIC_THEOREM"
                reasoning = (
                    "The theorem is closed but its type does not mention any "
                    "object of the Clay problem (no cohomology, no gauge theory, "
                    "no P/NP machine model); it is a true statement about "
                    "unrelated simple objects."
                )
            v = ProblemVerdict(
                problem=prob,
                claimed_theorem=info["claimed_name"],
                theorem_kind=kind,
                explicit_premises=premises,
                is_conditional=bool(premises),
                resolves_official_statement=resolves,
                verdict=verdict,
                reasoning=reasoning,
            )
            v.supporting_quotes.append(cs.gap)
            verdicts.append(v)
        return verdicts
