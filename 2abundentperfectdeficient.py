def sum_of_divisors(n):
    """Return the sum of proper divisors of n."""
    divisors_sum = 1  
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i: 
                divisors_sum += n // i
    return divisors_sum
def classify_number(n):
    """Classify the number as abundant, perfect, or deficient."""
    if n <= 0:
        return "Number must be positive."
    div_sum = sum_of_divisors(n)
    if div_sum == n:
        return "Perfect"
    elif div_sum > n:
        return "Abundant"
    else:
        return "Deficient"
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    classification = classify_number(number)
    print(f"The number {number} is {classification}.")
