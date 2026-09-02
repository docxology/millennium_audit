"""Real-data tests: assert audit facts against the extracted package files.

No mocks - every test reads the actual MillenniumLean package under audit.
"""
import json
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
PKG = HERE.parent / "package" / "MillenniumLean"
sys.path.insert(0, str(HERE.parent / "src"))

from evidence import EvidenceStore  # noqa: E402
from lean_parser import (
    extract_declaration_names, extract_axioms, extract_sorries,
    parse_declaration_binder_names,
)
from statement_audit import StatementAuditor
from clay_statements import CLAY_STATEMENTS
from verdicts import VERDICTS


@pytest.fixture(scope="module")
def store():
    return EvidenceStore(PKG)


@pytest.fixture(scope="module")
def mtext(store):
    return store.read("Millennium.lean")


@pytest.fixture(scope="module")
def ttext(store):
    return store.read("Tower.lean")


# ---------- package integrity ----------

def test_package_files_present(store):
    names = set(store.file_names())
    for required in ("Millennium.lean", "Tower.lean", "audit.py",
                     "PROOF_CERTIFICATE.md", "lakefile.toml"):
        assert required in names, f"missing {required}"


def test_toolchain_pinned(store):
    assert store.read("lean-toolchain").strip() == "leanprover/lean4:v4.34.0-rc1"


# ---------- kernel hygiene (their claims, independently re-derived) ----------

def test_no_live_sorry(mtext, ttext):
    assert extract_sorries(mtext) == []
    assert extract_sorries(ttext) == []


def test_no_project_axioms(mtext, ttext):
    assert extract_axioms(mtext) == []
    assert extract_axioms(ttext) == []


def test_declaration_counts(mtext, ttext):
    decls = extract_declaration_names(mtext) + extract_declaration_names(ttext)
    assert len(decls) == 41


# ---------- statement-level verdicts (the substance of the audit) ----------

@pytest.fixture(scope="module")
def verdicts(mtext):
    return StatementAuditor(CLAY_STATEMENTS, sys.modules['lean_parser']).audit(mtext)


def test_all_six_problems_audited(verdicts):
    assert len(verdicts) == 6
    assert {v.problem for v in verdicts} == set(CLAY_STATEMENTS)


def test_no_problem_resolved(verdicts):
    for v in verdicts:
        assert not v.resolves_official_statement, f"{v.problem} flagged resolved"


def test_riemann_conditional(verdicts):
    v = next(v for v in verdicts if v.problem == "Riemann")
    assert v.verdict == "CONDITIONAL_IMPLICATION"
    assert set(v.explicit_premises) == {"hD", "corr"}


def test_yang_mills_is_substitution(verdicts):
    v = next(v for v in verdicts if v.problem == "Yang-Mills")
    assert v.verdict == "CONDITIONAL_IMPLICATION"
    assert set(v.explicit_premises) == {"hc", "hid"}
    # the type is literally 0 < c -> m = c -> 0 < m
    assert "forall c m : Real, 0 < c -> m = c -> 0 < m" in CLAY_STATEMENTS["Yang-Mills"].claimed_type_summary


def test_ns_and_bsd_are_defs(verdicts):
    for prob in ("Navier-Stokes", "BSD"):
        v = next(v for v in verdicts if v.problem == v.problem)  # noqa
    ns = next(v for v in verdicts if v.problem == "Navier-Stokes")
    bsd = next(v for v in verdicts if v.problem == "BSD")
    assert ns.theorem_kind == "def"
    assert bsd.theorem_kind == "def"


def test_hodge_is_list_arithmetic(mtext):
    # hodge_kunneth's type must be the conv-identity, not cohomology
    assert "theorem hodge_kunneth : conv [1,1,1,1] [1,1,1] = [1,2,3,3,2,1]" in mtext


def test_tower_smoking_gun_literal(mtext, ttext):
    # the tower invariant is literally 0 < n + 1
    assert "def declInv (n : Nat) : Prop := 0 < n + 1" in ttext
    # Millennium.lean: the "Millennium theorems" take an explicit step premise
    # and reduce to Tower.universal over the 0 < n + 1 invariant
    for nm in ("hodge", "bsd", "navier_stokes"):
        assert f"theorem {nm} (step : ∀ n, Tower.declInv n → Tower.declInv (n+1))" in mtext
    # Tower.lean: the *_universal wrappers and the Poincare "control" all equal
    # Tower.universal over the same invariant
    for nm in ("hodge_universal", "bsd_universal", "ns_alldata",
               "riemann_allheights", "ym_alllevels", "poincare_control"):
        assert f"theorem {nm}" in ttext
        assert "universal " in ttext


def test_universal_is_succ_pos(ttext):
    # base case is Nat.succ_pos - i.e., 'n+1 > 0'
    assert "Nat.succ_pos" in ttext


def test_pvsnp_premises(verdicts):
    v = next(v for v in verdicts if v.problem == "P-vs-NP")
    assert set(v.explicit_premises) == {"hq", "hlb", "bridge"}


def test_report_json_written():
    report = HERE.parent / "data" / "audit_report.json"
    if report.exists():
        data = json.loads(report.read_text())
        assert all(not v["resolves_clay"] for v in data["verdicts"])
