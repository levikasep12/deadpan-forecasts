#!/usr/bin/env python3
"""One deadpan weather forecast for a city that does not exist.

Writes a single original forecast (<= 160 characters, one line) to
/output/entry.txt, exactly as the bounty requires. Standard library only,
no network, no input files, deterministic: every run writes the same bytes.

The forecast is written like a real broadcast line: a named invented city,
a concrete weather detail, and a deadpan twist that makes the place feel
real. Vexford's fog is so thick that even the streetlights cannot see
each other — so, deadpan logic says, they would introduce themselves.
"""

from pathlib import Path

# The forecast itself: one line, original, written for this entry.
LINE = (
    "In Vexford, expect fog so thick the streetlights have started "
    "introducing themselves to each other; visibility four metres, "
    "patience zero."
)

# Output path fixed by the bounty spec (absolute, not relative to cwd).
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LINE.strip()
    if not text or len(text) > 160 or "\n" in text:
        raise ValueError("line must be one line of 1-160 characters")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the line, no trailing newline: the file IS the forecast.
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
