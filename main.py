#!/usr/bin/env python3
"""The Printer Finally Answers — make.fun entry.

Writes one line, the office printer's comeback, to /output/entry.txt.
Fully offline and deterministic: no network, no randomness, no secrets.
"""

import os

# The printer's comeback — tournament winner (4/4 games, 2.85 pts of 4):
# judged pairwise by the Caffeine router against 9 other original lines
# using the house judge brief; see tournament.jsonl for every verdict.
LINE = "PAPER JAM IN TRAY 2. I put it there. I know where it is. I am not telling you."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    line = LINE
    # Self-check: one line, 1-240 characters, not only whitespace.
    assert 1 <= len(line) <= 240, f"line is {len(line)} chars, must be 1-240"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line.strip(), "line must not be only whitespace"
    assert line == line.strip(), "line must not start or end with whitespace"
    line.encode("utf-8")  # gate requires UTF-8 text
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # exactly the line, no trailing newline
    print(f"Wrote {len(line)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
