"""One Star, Five Stars for the Food (variant 2).

Writes a single-sentence alien tourist review of planet Earth to
/output/entry.txt: a one-star verdict whose only mercy is the food.
Pure Python 3.13 standard library, deterministic, no network.
"""

# One concrete incident only an outsider would file a complaint about
# (a two-hour queue and a customs form asking whether the visitor is a
# vegetable) and one specific food (charcoal-grilled corn dusted with
# chili and lime); the comic turn lands in the last clause.
ENTRY = (
    "One star: Earth made me queue two hours and fill in a form asking "
    "whether I am a vegetable, but the charcoal-grilled corn dusted "
    "with chili and lime was so good I nearly forgave the paperwork."
)

import os


def main() -> None:
    text = ENTRY.strip()
    # Gate (kit RULES.txt): UTF-8 text, 1 to 200 characters, not only
    # whitespace, and exactly one sentence.
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    if text != text.strip() or not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
