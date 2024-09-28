def reverse_words_in_string(s):
    """Reverse each word in the string but keep the order of words intact."""
    words = s.split()  
    reversed_words = [word[::-1] for word in words] 
    return ' '.join(reversed_words)  
input_string = input("Enter a string: ")
print(f"Reversed words: {reverse_words_in_string(input_string)}")
