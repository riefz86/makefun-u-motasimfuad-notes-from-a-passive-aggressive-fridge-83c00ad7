#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge.

One funny passive-aggressive note a smart fridge leaves for its owner.
Writes a single line (1-200 chars, UTF-8) to /output/entry.txt.

The note leans on the judge's brief: the fridge's voice, smug about its
door sensors and logs, petty about a small domestic habit, concrete detail
(the 47 seconds, the electric bill), and a sting at the end it never
explains.
"""

import os

NOTE = (
    "You left my door open for 47 seconds, stared, ate nothing, "
    "then blamed me for the electric bill. I have the logs."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NOTE)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
