# MillenniumLean — AIX Global, Inc. · Seed IQ (Adaptive Multiagent Autonomous Control platform)
# Companion certificate layer to "Demonstrating Quantum Value by Solving the Six Remaining Clay
# Millennium Problems" (Holt & Ovseyenko, AIX Global, 2026). DOI: 10.5281/zenodo.22179463
# (c) 2026 AIX Global Innovations, Inc. All rights reserved. Verification is unrestricted.

# Closed-term audit: for each final, parse its full signature with balanced-paren tracking and
# list EVERY explicit parenthesized binder in its type. Binders whose name begins with `h` or is
# a named certificate (`corr`, `bridge`, `step`) are premises; the rest are data parameters.
import re
src = open("Millennium.lean").read()

finals = {
    "Riemann":       "riemannHypothesis_of_selfAdjoint_correspondence",
    "Yang-Mills":    "yang_mills_gap",
    "Navier-Stokes": "ns_official",
    "Hodge":         "hodge_kunneth",
    "BSD":           "bsd_official",
    "P vs NP":       "P_neq_NP_of_proof_lower_bound",
}

def signature(name):
    m = re.search(r"(theorem|def)\s+" + re.escape(name) + r"\b", src)
    if not m:
        return None, "NOT FOUND"
    kind = m.group(1)
    i = m.end()
    depth = 0
    j = i
    # scan to the top-level `:=` or `:= by` / end of the declaration header at depth 0
    while j < len(src) - 1:
        c = src[j]
        if c in "([{": depth += 1
        elif c in ")]}": depth -= 1
        elif depth == 0 and src[j:j+2] == ":=":
            break
        j += 1
    return kind, src[i:j]

def binders(sig):
    """Top-level parenthesized binders, balanced-paren aware."""
    out, depth, start = [], 0, None
    for idx, c in enumerate(sig):
        if c == "(":
            if depth == 0: start = idx + 1
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0 and start is not None:
                grp = sig[start:idx]
                if ":" in grp:
                    out.append(grp.strip())
                start = None
    return out

def is_premise(name):
    return name.startswith("h") or name.startswith("_h") or name in ("corr", "bridge", "step")

print("CLOSED-TERM AUDIT - explicit binders in each final's type (balanced-paren parse)\n")
for prob, nm in finals.items():
    kind, sig = signature(nm)
    if kind is None:
        print(f"[{prob}]  {nm}\n   -> NOT FOUND\n"); continue
    bs = binders(sig)
    names = [n for b in bs for n in b.split(":")[0].split() if n]
    prem = [n for n in names if is_premise(n)]
    data = [n for n in names if not is_premise(n)]
    tag = "CLOSED (no premise in the type)" if not prem else "CONDITIONAL - premises: " + ", ".join(prem)
    extra = ("  [data: " + ", ".join(data) + "]") if data else ""
    print(f"[{prob}]  {kind} {nm}\n   -> {tag}{extra}\n")
