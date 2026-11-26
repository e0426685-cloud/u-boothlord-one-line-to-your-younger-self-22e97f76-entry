#!/usr/bin/env python3
"""One Line to Your Younger Self.

Writes a single line to /output/entry.txt (UTF-8, 1-200 chars, one line).
Python standard library only.
"""

import os

LINE = "The applause you're chasing comes from people you'd never take advice from \u2014 stop performing for an audience you don't respect."

OUTPUT_PATH = "/output/entry.txt"


def main():
    line = LINE.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"line is {len(line)} characters, must be 1-200")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if not line.strip():
        raise ValueError("line must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
