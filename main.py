"""One Word From Grandma — entry.

The word: "Doohickey".

Why this word: it is the word a grandma reaches for when she cannot
name the gadget in front of her — warm, a little baffled, and instantly
recognisable as her voice. Faced with AI, a machine she half understands
and wholly distrusts, she would not call it a robot or a computer; she
would call it the doohickey. One word, nine letters, no punctuation,
exactly as she would text it to a grandchild.
"""

import os

WORD = "Doohickey"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
