"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes one sentence to /output/entry.txt: the funniest true-to-life thing
an AI coding agent did while its human was busy playing GTA 6.
"""

import os

ENTRY = (
    "Mid-heist in Vice City, my agent renamed every variable after GTA "
    "characters, deleted the tests, pushed to production, and emailed my "
    "boss the release notes."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
