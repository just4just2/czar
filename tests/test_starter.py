"""Integration checks for the shipped, offline CLI. No third-party packages."""

import hashlib
import json
import shutil
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class StarterTests(unittest.TestCase):
    def test_pinned_upstream(self):
        vendor = ROOT / "vendor" / "ontoship"
        metadata = json.loads((vendor / "UPSTREAM.json").read_text(encoding="utf-8"))
        for name, expected in metadata["sha256_lf"].items():
            content = (vendor / name).read_bytes().replace(b"\r\n", b"\n")
            self.assertEqual(hashlib.sha256(content).hexdigest(), expected, name)

    def test_offline_memory_lifecycle(self):
        with tempfile.TemporaryDirectory(prefix="czar test ") as folder:
            project = Path(folder) / "project with spaces"
            for name in ("scripts", "vendor", "docs"):
                shutil.copytree(ROOT / name, project / name)
            (project / "sources").mkdir()
            (project / "sources" / "private.md").write_text("privatecanary", encoding="utf-8")
            (project / "unrelated.md").write_text("outsidecanary", encoding="utf-8")

            def run(*args, ok=True):
                # Run outside the checkout: paths must come from the script, not cwd.
                result = subprocess.run(
                    [sys.executable, "-S", str(project / "scripts" / "kb.py"), *args],
                    cwd=folder, capture_output=True, text=True, encoding="utf-8",
                )
                if ok:
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                else:
                    self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
                return result.stdout

            run("lint", "--strict")
            probe = project / "docs" / "probe.md"
            probe.write_text("# Check\n\nquartzcanary\n\nпамять проверка\n", encoding="utf-8")
            for query in ("quartzcanary", "память"):
                results = json.loads(run("search", query, "--json", "-k", "100"))
                self.assertIn("docs/probe.md", [item["path"] for item in results])
            database = project / ".gitmark" / "index.db"
            with closing(sqlite3.connect(database)) as connection:
                paths = [row[0] for row in connection.execute("SELECT path FROM files")]
                self.assertTrue(paths)
                self.assertTrue(all(path.startswith("docs/") for path in paths))

            probe.write_text("# Check\n\nzirconcanary\n", encoding="utf-8")
            updated = json.loads(run("search", "zirconcanary", "--json"))
            self.assertIn("docs/probe.md", [item["path"] for item in updated])
            with closing(sqlite3.connect(database)) as connection:
                bodies = connection.execute("SELECT body FROM fts WHERE path='docs/probe.md'").fetchall()
                self.assertNotIn("quartzcanary", str(bodies))

            probe.unlink()
            run("search", "память", "--json")
            with closing(sqlite3.connect(database)) as connection:
                self.assertEqual(connection.execute("SELECT count(*) FROM files WHERE path='docs/probe.md'").fetchone()[0], 0)

            run("map")
            page = (project / "docs" / "docs-map.html").read_text(encoding="utf-8")
            self.assertIn("<canvas", page)
            self.assertIn("docs/context.md", page)
            self.assertNotIn("privatecanary", page)
            self.assertNotIn("outsidecanary", page)

            broken = project / "docs" / "reference" / "broken.md"
            broken.write_text("# Broken\n\n[Missing](does-not-exist.md)\n", encoding="utf-8")
            output = run("lint", "--strict", ok=False)
            self.assertIn("I4", output)
            self.assertIn("I1", output)


if __name__ == "__main__":
    unittest.main()
