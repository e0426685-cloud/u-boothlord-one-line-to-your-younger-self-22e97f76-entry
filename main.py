"""One Line to Your Younger Self — make.fun entry.

Writes a single line to /output/entry.txt. Standard library only.
"""

import os

LINE = (
    "You were right to keep the notebook nobody read; "
    "one day every page in it becomes the proof you were paying attention."
)


def main():
    line = LINE.strip()
    if not line:
        raise ValueError("entry line is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(line))

    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    os.chmod(path, 0o644)
    print("wrote %d chars to %s" % (len(line), path))


if __name__ == "__main__":
    main()
