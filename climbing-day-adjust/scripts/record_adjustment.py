#!/usr/bin/env python3
"""Append a structured plan adjustment entry to a climbing journey document."""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


SECTION = "## Plan Adjustment Log"
INSERT_BEFORE = "## Plan History"


def build_entry(args: argparse.Namespace) -> str:
    lines = [
        f"### {args.date}",
        "",
        f"- Change type: {args.change_type}.",
    ]
    if args.from_day:
        lines.append(f"- From: {args.from_day}.")
    if args.to_day:
        lines.append(f"- To: {args.to_day}.")
    if args.reason:
        lines.append(f"- Reason: {args.reason}.")
    if args.change:
        lines.append(f"- Plan change: {args.change}.")
    if args.next_action:
        lines.append(f"- Next action: {args.next_action}.")
    lines.append("")
    return "\n".join(lines)


def append_entry(text: str, entry: str) -> str:
    if SECTION in text:
        head, tail = text.split(SECTION, 1)
        next_section_index = tail.find("\n## ")
        if next_section_index == -1:
            return f"{head}{SECTION}{tail.rstrip()}\n\n{entry}\n"

        section_body = tail[:next_section_index].rstrip()
        rest = tail[next_section_index:]
        return f"{head}{SECTION}{section_body}\n\n{entry}\n{rest}"

    if INSERT_BEFORE in text:
        head, tail = text.split(INSERT_BEFORE, 1)
        return f"{head.rstrip()}\n\n{SECTION}\n\n{entry}\n{INSERT_BEFORE}{tail}"

    return f"{text.rstrip()}\n\n{SECTION}\n\n{entry}\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("journey", type=Path)
    parser.add_argument(
        "--type",
        dest="change_type",
        required=True,
        choices=["skip", "swap", "harder", "softer", "recovery", "extra"],
    )
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--from-day", default="")
    parser.add_argument("--to-day", default="")
    parser.add_argument("--reason", default="")
    parser.add_argument("--change", default="")
    parser.add_argument("--next-action", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    path = args.journey.expanduser().resolve()
    text = path.read_text(encoding="utf-8")
    entry = build_entry(args)
    path.write_text(append_entry(text, entry), encoding="utf-8")
    print(f"Updated {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
