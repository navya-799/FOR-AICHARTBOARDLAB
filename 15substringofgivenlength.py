def print_even_length_substrings(s):
    length = len(s)
    for start in range(length):
        for end in range(start + 2, length + 1, 2):  
            print(s[start:end])
input_string = "python"
print_even_length_substrings(input_string)
