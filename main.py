#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — writes the entry line to /output/entry.txt."""

import os

ENTRY = "You will find the bug on your very last token, one line above the context limit."

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
