# Abstract

This report audits the MillenniumLean package (AIX Global, Inc.; Zenodo
DOI 10.5281/zenodo.22226553), which claims complete kernel-checked Lean 4
proofs of the six remaining Clay Millennium Problems. We read all eleven files
of the package verbatim, re-derived every kernel-hygiene claim independently
under the pinned toolchain (leanprover/lean4:v4.34.0-rc1; mathlib at the
manifest-pinned revision d0be1efe9a), and compared each claimed final theorem
against the official Clay problem statements.

Findings are itemized as fourteen one-per-finding reports (docs/audit/), each
quoting the package verbatim with line anchors and recording the probe that
backs the verdict. The kernel claims are TRUE and reproduce byte-for-byte:
clean build, zero live `sorry`, zero project axioms, axiom footprints inside
{propext, Classical.choice, Quot.sound}. They are also evidentially void: the
"final theorems" are either implications whose unproved premise binders carry
the entire mathematical content (Riemann, Yang-Mills, P vs NP), definitions
of the open statements (Navier-Stokes, BSD), or true theorems about unrelated
simple objects (a list identity for Hodge; substitution for Yang-Mills). The
"universalization tower" that certifies Hodge, BSD, and Navier-Stokes proves
only that 0 < n + 1 for all naturals. Verdict: none of the six problems is
resolved. The audit disputes no kernel output of the package; it disputes
what those outputs are claimed to demonstrate.

**Publication.** This report is published as a Zenodo record
(DOI 10.5281/zenodo.22243473) together with the complete evidence bundle -
all fourteen findings, the audit doctrine, the kernel reproduction receipt,
and the machine-readable audit report. The public paper copy with the
rendered PDF and full text lives in the docxology repository
(github.com/docxology/docxology, papers/2026_MillenniumAudit). The standalone repository for this audit is github.com/docxology/millennium_audit.
