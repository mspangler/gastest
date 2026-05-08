#!/usr/bin/env python3
"""Word frequency counter: prints the top N most common words in a text file."""

import argparse
import re
from collections import Counter


def count_words(text: str) -> Counter:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return Counter(words)


def main():
    parser = argparse.ArgumentParser(
        description="Print the top N most common words in a text file."
    )
    parser.add_argument("file", help="Path to input text file")
    parser.add_argument(
        "--top", type=int, default=10, metavar="N", help="Number of top words to show (default: 10)"
    )
    args = parser.parse_args()

    with open(args.file, encoding="utf-8") as f:
        text = f.read()

    counts = count_words(text)
    for word, freq in counts.most_common(args.top):
        print(f"{freq:>6}  {word}")


if __name__ == "__main__":
    main()
