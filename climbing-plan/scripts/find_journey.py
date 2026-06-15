#!/usr/bin/env python3
"""Find the most likely climbing journey Markdown file."""

from __future__ import annotations

import sys
from pathlib import Path


PREFERRED_NAMES = {
    "journey.md": 100,
    "climbing-journey.md": 90,
    "climb-journey.md": 85,
    "training-journey.md": 80,
}

SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules"}


def iter_markdown(root: Path):
    for path in root.rglob("*.md"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        yield path


def score(path: Path) -> int:
    name = path.name.lower()
    stem = path.stem.lower()
    value = PREFERRED_NAMES.get(name, 0)
    if "journey" in stem:
        value += 25
    if "climb" in stem or "training" in stem:
        value += 10
    if path.parent.name == "climbingcoach":
        value += 10
    return value


def main() -> int:
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    if not root.exists():
        print(f"Search root does not exist: {root}", file=sys.stderr)
        return 2

    candidates = sorted(iter_markdown(root), key=lambda item: (-score(item), str(item)))
    candidates = [item for item in candidates if score(item) > 0]
    if not candidates:
        print("No journey document found.", file=sys.stderr)
        return 1

    print(candidates[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
