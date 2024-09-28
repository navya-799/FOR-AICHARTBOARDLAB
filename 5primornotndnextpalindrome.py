def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def next_palindrome(n):
    """Find the next palindrome greater than n."""
    def is_palindrome(x):
        return str(x) == str(x)[::-1]
    while True:
        n += 1
        if is_palindrome(n):
            return n
number = int(input("Enter an integer: "))
if is_prime(number):
    print(f"{number} is a prime number.")
    print(f"Next palindrome: {next_palindrome(number)}")
else:
    print("Not prime.")
