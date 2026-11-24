#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes one pickup line, as spoken by a vending machine to a passing
human, to /output/entry.txt.

The line is validated before writing (one line, 1 to 200 characters,
valid UTF-8, not blank) and the file is read back afterwards to confirm
the written bytes match the line exactly.
"""

import os
import sys

LINE = "I only hum when you walk by. My coils dropped your chocolate twice this week, and both times were on purpose."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS} to {MAX_CHARS} characters, got {len(line)}"
        )
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    data = LINE.encode("utf-8")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "wb") as f:
        f.write(data)
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    if written != data:
        raise ValueError("read-back check failed: written bytes differ from the line")
    if len(written.decode("utf-8")) != len(LINE):
        raise ValueError("read-back check failed: character count mismatch")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
