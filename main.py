#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head.

Writes one one-line joke about office life to /output/entry.txt.
Deterministic, no network, no date dependence.
"""

import os

JOKE = "The broken lift sign says \u201cUse stairs for cardio,\u201d which is the first time HR has described a fire hazard as a wellness benefit."


def main() -> None:
    # Gate: the entry must be 1-200 UTF-8 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200 and JOKE.strip(), "joke fails the length gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
