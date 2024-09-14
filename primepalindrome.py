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

    num = n + 1
    while not is_palindrome(num):
        num += 1
    return num

def main():
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"Next palindrome after {number} is {next_palindrome(number)}")
        else:
            print("Not prime")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
