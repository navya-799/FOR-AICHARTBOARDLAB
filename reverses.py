def reverse_words(s):
    """Reverses each word in the given string."""
    return ' '.join(word[::-1] for word in s.split())

def main():
    s = input("Enter a string: ")
    print(reverse_words(s))

if __name__ == "__main__":
    main()
import numpy as np

def matrix_operations():
    # Input matrices
    a = np.array([[int(x) for x in input("Enter matrix A (space-separated, row by row): ").split()] for _ in range(2)])
    b = np.array([[int(x) for x in input("Enter matrix B (space-separated, row by row): ").split()] for _ in range(2)])
    
    # Choose operation
    operation = input("Choose operation (add/sub/mul/trace): ").strip().lower()
    
    if operation == 'add':
        result = a + b
        print("Result of addition:")
        print(result)
    
    elif operation == 'sub':
        result = a - b
        print("Result of subtraction:")
        print(result)
    
    elif operation == 'mul':
        result = np.dot(a, b)  # Matrix multiplication
        print("Result of multiplication:")
        print(result)
    
    elif operation == 'trace':
        print("Trace of matrix A:", np.trace(a))
        print("Trace of matrix B:", np.trace(b))
    
    else:
        print("Invalid operation")

if __name__ == "__main__":
    matrix_operations()
