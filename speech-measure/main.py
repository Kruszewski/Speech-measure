#!/usr/bin/env python3
import argparse
import textwrap

def measure_length_in_words(file_path):
    # Example function to measure length in words
    with open(file_path, 'r') as file:
        text = file.read()
    word_count = len(text.split())
    print(f"Word count: {word_count}")

def measure_character_count(file_path):
    # Example function to measure character count
    with open(file_path, 'r') as file:
        text = file.read()
    char_count = len(text)
    print(f"Character count: {char_count}")

def measure_length_in_seconds(file_path):
    # Example function to measure length in seconds
    # Assuming 150 words per minute as average speaking rate
    with open(file_path, 'r') as file:
        text = file.read()
    word_count = len(text.split())
    seconds = (word_count / 150) * 60
    print(f"Length in seconds: {seconds:.2f}")

def main():
    parser = argparse.ArgumentParser(
        description="Process some integers.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent("""Examples:
                            sm -l speech.txt # Measures speech length in words
                            sm -ch speech.txt # Measures character count
                            sm -t speech.txt # Measures speech length in seconds
        """),
    )
    parser.add_argument('file', help='File to process')
    parser.add_argument('-l', '--length', action='store_true', help='Measure speech length in words')
    parser.add_argument('-ch', '--character', action='store_true', help='Measure character count')
    parser.add_argument('-t', '--time', action='store_true', help='Measure speech length in seconds')

    args = parser.parse_args()
    if not args.length and not args.character and not args.time:
        parser.error("No option provided.")

    if args.length:
        measure_length_in_words(args.file)
    if args.character:
        measure_character_count(args.file)
    if args.time:
        measure_length_in_seconds(args.file)

if __name__ == "__main__":
    main()