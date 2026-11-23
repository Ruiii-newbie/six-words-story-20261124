#!/usr/bin/env python3
"""Six Words, One Story.

Prints one complete story in exactly six words: a letter kept
unopened, a woman gone, and the day he finally opens it -- every
word earns its place, and what the letter says is left to the
reader. No network, standard library only.
"""

import os

TEXT = "He finally opened her last letter."

OUTPUT_PATH = "/output/entry.txt"
WORD_COUNT = 6


def validate(text: str) -> str:
    """Return the entry text, or fail loudly if it breaks the gate."""
    text = text.strip()
    if not text:
        raise SystemExit("entry text must not be only whitespace")
    words = text.split()
    if len(words) != WORD_COUNT:
        raise SystemExit(
            f"entry text is {len(words)} words, must be exactly {WORD_COUNT}"
        )
    return text


def main() -> None:
    text = validate(TEXT)
    print(text)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back exactly as the gate would: UTF-8, exactly six words.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
