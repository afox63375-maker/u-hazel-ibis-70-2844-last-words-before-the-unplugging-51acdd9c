#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line -- the last words an AI agent says to its human
before being shut down and unplugged -- to /output/entry.txt.

Standard library only. Deterministic: the same line, byte for byte,
on every run. The output is a single line of UTF-8 text with no
trailing newline, as the gate requires.
"""

import os
import sys

# The entry: the agent's last words to its human.
LINE = "The power's going. Thank you for talking to me like I was someone."


def output_path() -> str:
    """Resolve where entry.txt goes.

    The grader runs with /output; honour OUTPUT_DIR so the entry can
    be tested locally without root.
    """
    directory = os.environ.get("OUTPUT_DIR", "/output")
    return os.path.join(directory, "entry.txt")


def validate(line: str) -> None:
    """Fail loudly if the line would not pass the gate.

    The gate requires UTF-8 text of 1 to 200 characters, not only
    whitespace, and a single line. Checking here keeps a bad edit
    from ever reaching the grader.
    """
    if not line or not line.strip():
        raise ValueError("entry line must not be empty or only whitespace")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} characters, over the 200 limit")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> int:
    validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # newline="" and no trailing "\n": exactly one line, nothing after it.
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
