#!/usr/bin/env python3
"""Real-Life Patch Notes entry: writes one patch-note line to /output/entry.txt.

The line is a release note for a real-life bug: the mouth auto-replying
'you too' to a waiter. Chosen from six candidates in CANDIDATES.md."""

LINE = "v2.6.8: fixed a bug where the mouth said 'you too' to the waiter who said 'enjoy your meal'. Auto-replies are now disabled by default."

# The gate: /output/entry.txt must hold 1 to 160 characters of real text,
# on a single line (the brief asks for one patch-note line, not a paragraph).
assert 1 <= len(LINE) <= 160 and LINE.strip(), "line must be 1-160 characters"
assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"

if __name__ == "__main__":
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
