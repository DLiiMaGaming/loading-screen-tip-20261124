#!/usr/bin/env python3
"""Loading Screen Gold entry writer.

Writes one loading-screen tip (a single line, at most 200 characters)
to /output/entry.txt. For local testing, pass an output path as argv[1].
"""

import sys
from pathlib import Path

ENTRY = "Your agent just refactored your code, your tests, and your confidence. Breathe: you're the only dependency it can't reinstall."

DEFAULT_OUTPUT = "/output/entry.txt"


def validate(text: str) -> None:
    """Fail loudly instead of writing an entry the gate would reject."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    out = Path(sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
