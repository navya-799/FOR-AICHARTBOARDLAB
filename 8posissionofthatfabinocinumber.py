def is_fibonacci(n):
    """Check if n is a Fibonacci number and find its position if true."""
    if n <= 0:
        return False, -1
    a, b, pos = 0, 1, 1
    while a < n:
        a, b = b, a + b
        pos += 1
    return a == n, pos if a == n else -1
number = int(input("Enter an integer: "))
is_fib, position = is_fibonacci(number)
if is_fib:
    print(f"{number} is a Fibonacci number at position {position}.")
else:
    print(f"{number} is not a Fibonacci number.")
