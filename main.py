#!/usr/bin/env python3
"""One Line to Your Younger Self.

Entry for the make.fun bounty "One Line to Your Younger Self":
a single piece of advice, written as one line, to the person you used to be.

The line chosen here tells younger-me to stop chasing applause from
people whose advice I would never take — a reminder that the audience
whose approval I craved is not an audience worth performing for.

Writes that line to /output/entry.txt (UTF-8, 1-200 chars, one line).
Python standard library only.
"""

import os

LINE = "The applause you're chasing comes from people you'd never take advice from \u2014 stop performing for an audience you don't respect."

OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check a candidate entry line and return the cleaned line.

    Raises ValueError unless the line is a single non-empty line of
    1-200 characters (leading/trailing whitespace is stripped first).
    """
    cleaned = line.strip()
    if not cleaned:
        raise ValueError("line must not be only whitespace")
    if len(cleaned) > 200:
        raise ValueError(f"line is {len(cleaned)} characters, must be 1-200")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("line must be a single line")
    return cleaned


def write_entry(line):
    """Write the validated line to OUTPUT_PATH as UTF-8, one line.

    Uses plain open() (not tempfile) and chmod 0644 so the grader,
    which may run as a different user, can read the file.
    """
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


def main():
    line = validate_line(LINE)
    write_entry(line)
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
