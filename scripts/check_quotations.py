#!/usr/bin/env python3
"""Quotation gate: verify every line-anchored quote in docs/audit/*.md byte-exact.

Layer 5 of the audit verification chain (docs/approach/audit-doctrine.md).
Parses each "> N: text" quote (and bare long quotes) in the audit findings
and checks line number and text against the extracted package bytes.

Usage: python3 scripts/check_quotations.py [docs/audit] [package/MillenniumLean]
Exit 0 iff all quotes verify.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
AUDIT_DIR = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "docs" / "audit"
PKG_DIR = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE.parent / "package" / "MillenniumLean"


def main() -> int:
    srcs = {f.name: f.read_text() for f in sorted(PKG_DIR.iterdir()) if f.is_file()}
    failures: list = []
    total = 0
    for md in sorted(AUDIT_DIR.glob("*.md")):
        for i, line in enumerate(md.read_text().splitlines(), 1):
            if not line.startswith("> "):
                continue
            q = line[2:].strip()
            m = re.match(r"^(\d+): (.*)$", q)
            if m:  # line-anchored quote: verify line number AND text
                total += 1
                ln, txt = int(m.group(1)), m.group(2)
                ok = any(
                    0 < ln <= len(t.splitlines()) and t.splitlines()[ln - 1] == txt
                    for t in srcs.values()
                )
                if not ok:
                    failures.append((md.name, i, ln, txt[:80]))
            elif len(q) >= 15 and "..." not in q:  # bare quote: substring match
                total += 1
                if not any(q in t for t in srcs.values()):
                    failures.append((md.name, i, "-", q[:80]))
    print(f"checked {total} quoted lines; failures: {len(failures)}")
    for f in failures:
        print("  FAIL:", f)
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
