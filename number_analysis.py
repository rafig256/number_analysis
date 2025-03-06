def prime_factors(n):
    """Returns the list of prime factors of a given number."""
    factors = []
    
    # Check for factor of 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors
    for divisor in range(3, int(n ** 0.5) + 1, 2):
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor

    if n > 1:
        factors.append(n)

    return factors

def main():
    try:
        number = int(input("Enter a number to factorize: "))
        if number <= 1:
            print("Please enter an integer greater than 1.")
            return

        result = prime_factors(number)
        print(f"The prime factors of {number} are: {result}")

        # اگر فقط یک فاکتور داشت، یعنی عدد ورودی اول است
        if len(result) == 1:
            print("This number is a prime number.")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    main()
