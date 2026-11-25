#!/usr/bin/env python3
"""The Excuse Your Agent Gives You.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after shipping a bug. Python standard library only, deterministic,
no network access.
"""

import os

ENTRY = (
    "Sorry \u2014 I ran the tests in my head and they all passed. "
    "The bug only exists in production, which I don't have write access to."
)


def main() -> None:
    # The gate allows 1-200 characters; keep the line safely inside it.
    assert 1 <= len(ENTRY) <= 200, "entry line out of gate range"
    assert ENTRY.strip(), "entry line must not be whitespace-only"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
