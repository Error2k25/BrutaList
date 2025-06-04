import itertools
import random
from collections import Counter

def generate_limited_wordlist():
    raw_input = input("Enter the characters to use (e.g., abc123@#): ").strip()
    if not raw_input:
        print("No characters provided. Exiting.")
        return

    char_counter = Counter(raw_input)
    charset_list = list(raw_input)
    charset_length = len(charset_list)

    min_len = int(input("Enter minimum length of combinations: ").strip())
    max_len = charset_length  # can't build longer combos than input length

    combinations = set()

    for length in range(min_len, max_len + 1):
        # Use multiset-aware permutations by generating and filtering
        for p in set(itertools.permutations(charset_list, length)):
            # Count characters in this permutation
            p_count = Counter(p)
            # Make sure we don't use any char more than original input
            if all(p_count[c] <= char_counter[c] for c in p_count):
                combinations.add(''.join(p))

    combinations = list(combinations)
    print(f"Total valid shuffled combinations: {len(combinations)}")

    print("Shuffling combinations...")
    random.shuffle(combinations)

    output_file = "BrutaList.txt"
    with open(output_file, "w") as f:
        for word in combinations:
            f.write(word + '\n')

    print(f"\nShuffled wordlist saved to '{output_file}'.")

if __name__ == "__main__":
    generate_limited_wordlist()
