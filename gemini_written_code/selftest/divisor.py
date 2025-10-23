import math

def divisor(n: int) -> int:
    # As per the example `assert divisor(15) == 4`, we assume `n` will be a positive integer (n >= 1).
    # The problem typically refers to positive divisors for positive integers.
    
    count = 0
    # Iterate from 1 up to the integer square root of n (inclusive).
    # Using math.isqrt for efficient integer square root calculation.
    limit = math.isqrt(n)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            # If i is a divisor of n
            if i * i == n:
                # If i is the square root of n, it's counted only once (e.g., 3 for 9)
                count += 1
            else:
                # Otherwise, i and n // i are two distinct divisors (e.g., 2 and 6 for 12)
                count += 2
                
    return count