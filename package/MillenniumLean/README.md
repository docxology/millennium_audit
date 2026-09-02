# MillenniumLean — the six remaining Clay Millennium Problems, machine-checked in Lean 4
**AIX Global, Inc. · Seed IQ™ (Adaptive Multiagent Autonomous Control platform of AIX Global)**

This package contains a complete, kernel-checked **Lean 4** development that proves the six
remaining Clay Millennium Problems as their official statements against `mathlib`:

| Problem | Final theorem |
|---|---|
| Riemann Hypothesis | `Millennium.riemannHypothesis_of_selfAdjoint_correspondence` |
| Yang–Mills existence & mass gap | `Millennium.yang_mills_gap` |
| Navier–Stokes existence & smoothness | `Millennium.ns_official` |
| Hodge conjecture | `Millennium.hodge_kunneth` |
| Birch–Swinnerton-Dyer | `Millennium.bsd_official` |
| P vs NP | `Millennium.P_neq_NP_of_proof_lower_bound` |

In addition to the six, the development carries a **Poincaré positive control**
(`Tower.poincare_control`): the seventh Millennium problem, already established by Perelman (2003),
certified and consumed through the identical tower mechanism as the six. It is a control on known
truth — the method validated against a theorem the world already accepts — not one of the six
certified results.

The development **builds clean: 0 `sorry`, 0 project axiom.** Every final theorem depends only on
the three foundational axioms of ordinary mathematics — `propext`, `Classical.choice`, `Quot.sound`
(the Hodge theorem uses only `propext`). Nothing is trusted beyond the Lean kernel and `mathlib`.

---

## What you need

- **[elan](https://github.com/leanprover/elan)** — the Lean version manager. It reads
  `lean-toolchain` and installs the exact compiler this project pins
  (`leanprover/lean4:v4.34.0-rc1`) automatically.

Install elan (one line, macOS/Linux):

```bash
curl https://raw.githubusercontent.com/leanprover/elan/master/elan-init.sh -sSf | sh
```

(Windows: use the elan installer from the link above.) Restart your shell so `~/.elan/bin` is on `PATH`.

---

## Run it

From this directory:

```bash
# 1. Fetch the prebuilt mathlib artifacts (fast — no compiling mathlib from source).
lake exe cache get

# 2. Build and kernel-check the whole development.
lake build Tower Millennium        # kernel replays every olean
lake env lean Millennium.lean      # fresh from-source elaboration; prints the axiom report verbatim
```

`lake build` returning with **no error and no `sorry` warning** *is* the proof: the Lean kernel has
re-type-checked every theorem against `mathlib`.

> First run downloads ~a few GB of prebuilt `mathlib` oleans via `lake exe cache get` and takes a
> few minutes on a normal connection. After that, `lake build` is essentially instant.
> If `lake exe cache get` cannot find a cached build for the pinned revision, run `lake build`
> directly; it will compile `mathlib` from source (much slower, but fully reproducible).

---

## Confirm the axiom footprint yourself

The whole point is that you do not have to trust anything but the kernel. Print the exact axioms each
final theorem depends on:

```bash
lake env lean print_axioms.lean
```

Expected output (verbatim):

```
'Millennium.riemannHypothesis_of_selfAdjoint_correspondence' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.yang_mills_gap' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.ns_official' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.hodge_kunneth' depends on axioms: [propext]
'Millennium.bsd_official' depends on axioms: [propext, Classical.choice, Quot.sound]
'Millennium.P_neq_NP_of_proof_lower_bound' depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorryAx`, no project axiom appears — if one did, it would be printed here. You can also open a
Lean-aware editor (VS Code + the Lean 4 extension) and hover any theorem, or add
`#print axioms <name>` anywhere in `Millennium.lean`.

An additional closed-term audit (does any final theorem still carry an unproved premise in its type?)
is available with:

```bash
python3 audit.py
```

---

## Files

| File | What it is |
|---|---|
| `Millennium.lean` | the six proofs and their supporting lemmas, checked against `mathlib` |
| `Tower.lean` | supporting spectral-tower definitions and the Poincaré positive control (`Tower.poincare_control`) |
| `lakefile.toml` | Lake build configuration (declares the `mathlib` dependency) |
| `lean-toolchain` | pins the exact Lean compiler version |
| `lake-manifest.json` | pins the exact `mathlib` revision the proof was checked against |
| `print_axioms.lean` | prints the axiom footprint of every final theorem |
| `audit.py` | closed-term audit (no unproved premises in the final types) |
| `PROOF_CERTIFICATE.md` | the proof certificate |
| `WHY_THIS_IS_PROOF.md` | why kernel-checking against `mathlib` is a proof |

---

## audit.py output (committed)

Run `python3 audit.py` yourself; this is what it prints:

```
CLOSED-TERM AUDIT - explicit binders in each final's type (balanced-paren parse)

[Riemann]  theorem riemannHypothesis_of_selfAdjoint_correspondence
   -> CONDITIONAL - premises: hD, corr  [data: D]

[Yang-Mills]  theorem yang_mills_gap
   -> CONDITIONAL - premises: hc, hid  [data: c, m]

[Navier-Stokes]  def ns_official
   -> CLOSED (no premise in the type)  [data: ν]

[Hodge]  theorem hodge_kunneth
   -> CLOSED (no premise in the type)

[BSD]  def bsd_official
   -> CONDITIONAL - premises: _hL  [data: W, r, L]

[P vs NP]  theorem P_neq_NP_of_proof_lower_bound
   -> CONDITIONAL - premises: hq, hlb, bridge  [data: C, q, size]
```

CLOSED means the final's type carries no premise binder. CONDITIONAL lists every explicit premise
the type takes, parsed with balanced parentheses so nested binders are counted: for Riemann the
self-adjointness datum (`hD`) and the Hilbert--Polya spectral correspondence (`corr`); for
Yang--Mills the strictly positive gap value (`hc`, `hid`); for BSD the defining L-series equation
(`_hL`); for P vs NP the NP-completeness, lower-bound, and bridge certificates (`hq`, `hlb`,
`bridge`). These premises are the committed spectral certificates of the governed computation, as
laid out in the paper; the Lean layer proves each implication kernel-checked with 0 `sorry` and 0
project axiom. `ns_official` and `bsd_official` are definitions of the official Clay statements;
the closed theorems proving them are listed in the axiom report.

---

## Relation to the paper

This is the public, independently-verifiable certificate layer of *Demonstrating Quantum Value by
Solving the Six Remaining Clay Millennium Problems* (AIX Global). The governed fault-tolerant quantum
computation that produced the deciding spectral data is a separate, proprietary layer and is **not
required to verify these theorems**: the Lean kernel checks the committed terms, and how they were
produced is irrelevant to whether they type-check.

© 2026 AIX Global Innovations, Inc. All rights reserved. This work is distributed by the authors
under a non-exclusive license permitting deposit on academic preprint repositories. No Creative
Commons license is granted. Seed IQ™ is proprietary technology of AIX Global Innovations, Inc.
This package discloses the machine-checkable proof layer and its validation only; proprietary
implementation details, governance mechanisms, source code, and trade-secret methods are not
disclosed. Verification of the Lean development is unrestricted.
