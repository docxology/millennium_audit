#!/usr/bin/env python3
"""Run the MillenniumLean source audit and write its report."""

import argparse
import json
import os
import sys
from pathlib import Path
from tempfile import NamedTemporaryFile

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
DEFAULT_REPORT = HERE.parent / "data" / "audit_report.json"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", nargs="?", type=Path, default=DEFAULT_PKG)
    parser.add_argument("--output", type=Path, help="Path for the report JSON.")
    args = parser.parse_args()
    pkg = args.package
    is_reference = pkg.resolve() == DEFAULT_PKG.resolve()
    out_path = args.output
    if out_path is None:
        out_path = DEFAULT_REPORT if is_reference else HERE.parent / "output" / "alternate-audit-report.json"
    if not is_reference and out_path.resolve() == DEFAULT_REPORT.resolve():
        parser.error("Choose a separate report path for an alternate package.")

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
    out_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = NamedTemporaryFile(mode="w", encoding="utf-8", dir=out_path.parent, delete=False)
    try:
        with temporary:
            json.dump(out, temporary, indent=2)
        os.replace(temporary.name, out_path)
    finally:
        Path(temporary.name).unlink(missing_ok=True)
    print(f"\nWrote {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
