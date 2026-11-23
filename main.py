#!/usr/bin/env python3
"""The Demo Punchline — make.fun bounty entry.

Writes one line to /output/entry.txt: a one-line joke about working
beside an AI coding agent, built for a room watching a demo.

The joke is deterministic: the same line, byte for byte, every run.
No network, no randomness, no arguments.

Why this line: the demo never crashes on the code anyone reviewed —
it crashes on the one line both the agent and the human skipped,
which is exactly the line an AI coding agent makes easiest to skip.
"""

from pathlib import Path

JOKE = (
    "My AI coding agent writes the code, I take the credit, "
    "and the demo always crashes on the one line neither of us "
    "bothered to read."
)


def main() -> None:
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    text = JOKE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 280, "entry must be 1-280 characters"
    output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
