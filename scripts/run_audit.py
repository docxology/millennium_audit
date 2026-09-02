#!/usr/bin/env python3
"""Thin orchestrator: run the full Millennium_Audit and print the report.

Usage: python3 scripts/run_audit.py [path/to/MillenniumLean]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "src"))

from evidence import EvidenceStore           # noqa: E402
from lean_parser import (                    # noqa: E402
    extract_declaration_names, extract_axioms, extract_sorries,
)
from statement_audit import StatementAuditor  # noqa: E402
from clay_statements import CLAY_STATEMENTS    # noqa: E402
from verdicts import VERDICTS                  # noqa: E402

DEFAULT_PKG = HERE.parent / "package" / "MillenniumLean"


def main() -> int:
    pkg = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_PKG
    store = EvidenceStore(pkg)
    mtext = store.read("Millennium.lean")
    ttext = store.read("Tower.lean")

    print("=" * 72)
    print("MILLENNIUM_AUDIT - forensic audit of MillenniumLean (AIX Global)")
    print("=" * 72)

    inv = store.inventory()
    print(f"\n[1] Package inventory: {len(inv)} files")
    for name, meta in inv.items():
        print(f"    {name:28s} {meta['bytes']:6d}B  {meta['lines']:4d} lines  {meta['sha256'][:12]}...")

    decls = extract_declaration_names(mtext) + extract_declaration_names(ttext)
    axioms = extract_axioms(mtext) + extract_axioms(ttext)
    sorries = extract_sorries(mtext) + extract_sorries(ttext)
    print(f"\n[2] Kernel hygiene (real grep): {len(decls)} declarations, "
          f"{len(axioms)} project axioms, {len(sorries)} sorry lines")

    auditor = StatementAuditor(CLAY_STATEMENTS, sys.modules['lean_parser'])
    verdicts = auditor.audit(mtext)
    print("\n[3] Statement-level verdicts:")
    for v in verdicts:
        print(f"\n  --- {v.problem} ({v.claimed_theorem}) [{v.theorem_kind}]")
        print(f"      verdict: {v.verdict}  premises: {v.explicit_premises}")
        print(f"      {v.reasoning}")

    print("\n[4] Smoking gun (Tower.lean:11):")
    print(f"    {VERDICTS['tower_smoking_gun']}")

    print("\n[5] Headline verdict:")
    print(f"    {VERDICTS['headline']}")

    print("\n[6] Epistemic status:")
    print(f"    {VERDICTS['epistemic_status']}")

    # Machine-readable record
    out = {
        "inventory": inv,
        "declarations": len(decls),
        "project_axioms": axioms,
        "sorries": len(sorries),
        "verdicts": [
            {
                "problem": v.problem,
                "claimed_theorem": v.claimed_theorem,
                "kind": v.theorem_kind,
                "premises": v.explicit_premises,
                "verdict": v.verdict,
                "resolves_clay": v.resolves_official_statement,
            }
            for v in verdicts
        ],
        "headline": VERDICTS["headline"],
    }
    out_path = HERE.parent / "data" / "audit_report.json"
    out_path.write_text(json.dumps(out, indent=2))
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
