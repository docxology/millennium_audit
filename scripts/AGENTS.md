# scripts/ - Agent Notes

Thin-orchestrator rule: scripts delegate to `../src/` modules and do I/O
only. No business logic here. `run_audit.py` inserts `../src/` on sys.path
by design (project-local import, no package installation).
