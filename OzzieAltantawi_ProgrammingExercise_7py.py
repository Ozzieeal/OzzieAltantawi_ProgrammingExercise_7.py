# OzzieAltantawi_ProgrammingExercise_7.py
# This program takes a paragraph input, including sentences with numbers or abbreviations,
# and correctly identifies individual sentences using regex look-ahead.

import re

def split_sentences(paragraph):
    """
    Splits a paragraph into sentences.
    Sentences may start with capital letters or numbers,
    and punctuation at the end is optional.
    """
    # Regex:
    # [A-Z0-9] -> start with capital letter or number
    # .*?       -> non-greedy match any characters
    # [.!?]?    -> optional punctuation at the end
    # (?=\s[A-Z0-9]|$) -> look-ahead: followed by space + capital/number OR end of string
    pattern = r'[A-Z0-9].*?[.!?]?(?=\s[A-Z0-9]|$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

def display_sentences(sentences):
    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}: {sentence.strip()}")
    print(f"\nTotal number of sentences: {len(sentences)}")

def main():
    paragraph = input("Enter a paragraph (sentences may begin with numbers or contain abbreviations): ")
    sentences = split_sentences(paragraph)
    display_sentences(sentences)

if __name__ == "__main__":
    main()
