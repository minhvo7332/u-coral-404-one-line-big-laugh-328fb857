#!/usr/bin/env python3
"""One Line, Big Laugh — v1 probe entry.

Writes a single funny line (<=200 chars) to /output/entry.txt.
Deterministic: fixed text, no randomness, network, or clock.
Stdlib only.
"""
import os

LINE = "My horoscope said I'd meet my soulmate today, so I stayed home. I don't want to meet me."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
