"""Parse Lean 4 source files: extract declaration signatures and binder names.

Real text parsing of the package under audit - no mocks.
"""
import re


def extract_declaration_names(lean_text: str) -> list:
    """All declared theorem/def/axiom names in a Lean source string."""
    names = re.findall(r"^(?:theorem|def|axiom|lemma|abbrev)\s+([A-Za-z_][A-Za-z0-9_']*)", lean_text, re.M)
    return names


def extract_axioms(lean_text: str) -> list:
    """Explicit `axiom` declarations (project axioms)."""
    return re.findall(r"^axiom\s+([A-Za-z_][A-Za-z0-9_']*)", lean_text, re.M)


def _strip_lean_comments(text: str) -> str:
    """Remove /- ... -/ block comments and -- line comments, preserving line counts."""
    out_lines = []
    in_block = False
    for line in text.splitlines():
        res, i, in_blk = [], 0, in_block
        while i < len(line):
            if in_blk:
                end = line.find("-/", i)
                if end == -1:
                    i = len(line)
                else:
                    in_blk = False
                    i = end + 2
            else:
                b = line.find("/-", i)
                l = line.find("--", i)
                if b == -1 and l == -1:
                    res.append(line[i:])
                    i = len(line)
                elif b != -1 and (l == -1 or b < l):
                    res.append(line[i:b])
                    i = b + 2
                    in_blk = True
                else:
                    res.append(line[i:l])
                    i = len(line)
        out_lines.append("".join(res))
        in_block = in_blk
    return "\n".join(out_lines)


def extract_sorries(lean_text: str) -> list:
    """Lines containing a live sorry tactic (comments stripped first)."""
    stripped = _strip_lean_comments(lean_text)
    out = []
    for i, line in enumerate(stripped.splitlines(), 1):
        if re.search(r"\bsorry\b", line):
            out.append((i, line.strip()))
    return out


def parse_declaration_binder_names(lean_text: str, decl_name: str):
    """Parse one declaration's header, returning (kind, binder names, premise names).

    Mirrors audit.py's balanced-paren logic but records all binder names and
    classifies premise vs data using the same heuristic as audit.py.
    """
    m = re.search(r"(theorem|def)\s+" + re.escape(decl_name) + r"\b", lean_text)
    if not m:
        return None, [], []
    kind = m.group(1)
    i = m.end()
    depth = 0
    j = i
    while j < len(lean_text) - 1:
        c = lean_text[j]
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif depth == 0 and lean_text[j:j+2] == ":=":
            break
        j += 1
    sig = lean_text[i:j]

    # top-level parenthesized binder groups
    groups, d, start = [], 0, None
    for idx, c in enumerate(sig):
        if c == "(":
            if d == 0:
                start = idx + 1
            d += 1
        elif c == ")":
            d -= 1
            if d == 0 and start is not None:
                grp = sig[start:idx]
                if ":" in grp:
                    groups.append(grp.strip())
                start = None
    names = []
    for grp in groups:
        head = grp.split(":")[0].strip()
        for n in head.split():
            if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_']*", n):
                names.append(n)
    premise_markers = ("h", "_h", "corr", "bridge", "step", "hlb", "attr", "hc", "hid")
    premises = [n for n in names if any(n.startswith(p) or n == p for p in premise_markers)]
    data = [n for n in names if n not in premises]
    return kind, names, {"premises": premises, "data": data}


def extract_final_theorems(lean_text: str, finals: dict) -> dict:
    """For each problem -> claimed final name, return parsed signature facts."""
    out = {}
    for prob, name in finals.items():
        kind, names, split = parse_declaration_binder_names(lean_text, name)
        out[prob] = {
            "claimed_name": name,
            "kind": kind,
            "binder_names": names,
            "premises": split["premises"],
            "data": split["data"],
            "found": kind is not None,
        }
    return out
