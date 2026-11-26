# Verification

The native suite checks the working package and verifies the archived quotations.

    uv sync --locked
    uv run --locked pytest

Coverage of the assertions: package integrity (files, toolchain pin), kernel
hygiene (0 sorry, 0 axioms, 41 declarations), statement verdicts (all six
problems classified, none resolved), the tower smoking gun (literal source
lines), the machine-readable report, and alternate-output isolation.
