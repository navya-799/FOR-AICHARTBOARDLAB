def digit_sum(n):
    """Calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))
def lucky_number(dob):
    """Calculate the lucky number from a date of birth."""
    day, month, year = dob.split('/')
    total_sum = digit_sum(day) + digit_sum(month) + digit_sum(year)
    while total_sum >= 10:
        total_sum = digit_sum(total_sum)
    return total_sum
dob = input("Enter your date of birth (DD/MM/YY): ")
print(f"Your lucky number is: {lucky_number(dob)}")
