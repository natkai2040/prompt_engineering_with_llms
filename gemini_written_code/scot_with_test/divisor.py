import math

def divisor(n):
    if not isinstance(n, int) or n <= 0:
        # As per common understanding and test case, assume n is a positive integer.
        # Raise an error or return a specific value for invalid input if necessary.
        # For this problem, we'll assume valid positive integer input.
        # If n=0, it has infinite divisors.
        # If n is negative, divisors are typically for its absolute value.
        # For this solution, assume n > 0.
        return 0 # Or raise ValueError("Input must be a positive integer")

    count = 0
    # Iterate from 1 up to the square root of n
    # We use int(math.sqrt(n)) + 1 to include the square root itself
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If i is a divisor, then n // i is also a divisor
            if i * i == n:
                # If i is the square root, it's counted only once
                count += 1
            else:
                # Otherwise, i and n // i are two distinct divisors
                count += 2
    return count