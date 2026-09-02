# tests/

15 real-data tests asserting audit facts against the extracted package.

    .venv/bin/python -m pytest tests/ -q

Coverage of the assertions: package integrity (files, toolchain pin), kernel
hygiene (0 sorry, 0 axioms, 41 declarations), statement verdicts (all six
problems classified, none resolved), the tower smoking gun (literal source
lines), and the machine-readable report.
