from collections import Counter
def count_characters(s):
    counts = Counter(s)
    for char, count in counts.items():
        print(f"'{char}': {count}")
input_string = "navya"
count_characters(input_string)
