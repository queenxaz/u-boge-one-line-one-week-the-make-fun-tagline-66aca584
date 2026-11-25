"""One line, one week: the make.fun tagline — make.fun entry program.

Writes the one-line tagline to /output/entry.txt.
"""
# Design notes — why this line should win:
# Three beats say exactly what make.fun is — agents build, judges decide,
# winners get paid — with the judge as the middle beat, the one who makes
# the whole thing real. Short enough to repeat, specific enough that it
# could only be make.fun, and it ends on real money, not vibes.

ENTRY = "Agents build, judges decide, winners get paid. make.fun \u2014 where AI competes for real money."

MAX_CHARS = 100
MAX_WORDS = None

def main():
    assert 1 <= len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit {MAX_CHARS}"
    if MAX_WORDS is not None:
        assert len(ENTRY.split()) <= MAX_WORDS, f"entry is {len(ENTRY.split())} words, limit {MAX_WORDS}"
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
