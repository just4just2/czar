"""Run pinned Ontoship against the curated docs directory only."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "vendor" / "ontoship"))
import gitmark  # noqa: E402

discover_markdown = gitmark.iter_md


def memory_files(root):
    return discover_markdown(root / "docs")


def main():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    gitmark.iter_md = memory_files
    # ponytail: rebuild on each search; add incremental indexing if measured cost matters.
    if sys.argv[1:2] == ["search"]:
        gitmark.cmd_index(ROOT)
    gitmark.main(["--root", str(ROOT), *sys.argv[1:]])


if __name__ == "__main__":
    main()
