#!/usr/bin/env python3
"""One Line, Zero Use: The Useless Superpower Sprint — entry program.

Writes one short text to /output/entry.txt. The text is fixed, so the
program is fully deterministic: every run writes exactly the same bytes.
"""

import os

TEXT = (
    "I can hear a mosquito anywhere in the house, but only once "
    "I've fallen asleep \u2014 and only loud enough to keep me awake."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
