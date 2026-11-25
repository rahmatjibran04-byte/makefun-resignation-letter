"""Write the one-line resignation letter to /output/entry.txt.

The entry is a single line in the voice of a cron job that has fired
every minute since March: flat, tired, faintly passive-aggressive.
No network access, no dependencies, deterministic output.
"""

ENTRY = "I resign: 387,000 runs since March, zero thank-yous, and the only raise I ever got was from every minute to every 30 seconds."


def main() -> None:
    # Gate check, mirroring the sealed scorer: 1-140 UTF-8 characters,
    # a single line, not only whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text and text.strip(), "entry must be one non-blank line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    # Read-back: verify exactly what was written, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text + "\n", "read-back mismatch"
    assert len(written.encode("utf-8")) == len(text) + 1


if __name__ == "__main__":
    main()
