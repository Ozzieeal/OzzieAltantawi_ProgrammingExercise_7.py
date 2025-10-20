# OzzieAltantawi_ProgrammingExercise_7.py
# This program takes a paragraph input, including sentences with numbers or abbreviations,
# and correctly identifies individual sentences using regex look-ahead.

import re

# Function to split paragraph into sentences
def split_sentences(paragraph):
    # Regex pattern explanation:
    # [A-Z] -> first character of sentence is capital letter
    # .*?   -> match any number of characters (non-greedy)
    # [.!?] -> sentence-ending punctuation
    # (?=\s[A-Z]|$) -> look-ahead: punctuation is followed by space + capital letter OR end of string
    pattern = r'[A-Z].*?[.!?](?=\s[A-Z]|$)'
    sentences = re.findall(pattern, paragraph, flags=re.DOTALL | re.MULTILINE)
    return sentences

# Function to display sentences and count
def display_sentences(sentences):
    print("\n--- Individual Sentences ---")
    for i, sentence in enumerate(sentences, start=1):
        print(f"{i}: {sentence}")
    print(f"\nTotal number of sentences: {len(sentences)}")

# Main function
def main():
    paragraph = input("Enter a paragraph (sentences may begin with numbers or contain abbreviations): ")
    sentences = split_sentences(paragraph)
    display_sentences(sentences)

# Run the program
if __name__ == "__main__":
    main()
