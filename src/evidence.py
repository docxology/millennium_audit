"""Evidence store: load and hash the package under audit. Real files only."""
import hashlib
import json
from pathlib import Path


class EvidenceStore:
    """Loads the audited package, records hashes, exposes file texts."""

    def __init__(self, pkg_dir):
        self.pkg_dir = Path(pkg_dir)
        if not self.pkg_dir.is_dir():
            raise FileNotFoundError(f"package dir missing: {self.pkg_dir}")
        self._hashes = {}
        for f in sorted(self.pkg_dir.glob("*")):
            if f.is_file():
                self._hashes[f.name] = hashlib.sha256(f.read_bytes()).hexdigest()

    def file_names(self):
        return sorted(self._hashes)

    def sha256(self, name):
        return self._hashes[name]

    def read(self, name):
        return (self.pkg_dir / name).read_text()

    def hashes_json(self):
        return json.dumps(self._hashes, indent=2, sort_keys=True)

    def inventory(self):
        inv = {}
        for name in self.file_names():
            text = self.read(name)
            inv[name] = {
                "sha256": self._hashes[name],
                "lines": text.count("\n"),
                "bytes": len(text.encode()),
            }
        return inv
