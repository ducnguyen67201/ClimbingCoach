#!/usr/bin/env python3
"""Scan text files for accidental banned brand wording."""

from __future__ import annotations

import sys
from pathlib import Path


BLOCKED_TERMS = [bytes.fromhex("6c617474696365").decode("ascii")]
SKIP_DIRS = {".git", ".venv", "__pycache__", "node_modules"}
TEXT_SUFFIXES = {".md", ".txt", ".yaml", ".yml", ".py", ".toml", ".json"}


def iter_text_files(root: Path):
    if root.is_file():
        yield root
        return

    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            yield path


def main() -> int:
    root = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else Path.cwd()
    root = root.resolve()
    failures = []

    for path in iter_text_files(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        lowered = text.lower()
        for term in BLOCKED_TERMS:
            if term.lower() in lowered:
                failures.append(path)
                break

    if failures:
        print("Found banned brand wording in:")
        for path in failures:
            print(f"- {path}")
        return 1

    print("OK: no banned brand wording found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
