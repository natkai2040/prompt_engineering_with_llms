import math

def divisor(n):
    if n == 0:
        return 0
    if n < 0:
        n = abs(n)
    
    count = 0
    # Iterate up to the integer square root of n
    # For each divisor i, n/i is also a divisor.
    # We only need to check up to sqrt(n) because if i > sqrt(n), then n/i < sqrt(n),
    # and we would have already found n/i.
    
    # math.isqrt(n) returns the integer part of the square root of n.
    limit = math.isqrt(n)
    
    for i in range(1, limit + 1):
        if n % i == 0:
            # If i*i == n, then i is the square root, and n/i is the same as i.
            # We count it once.
            if i * i == n:
                count += 1
            # Otherwise, i and n/i are distinct divisors.
            # We count both of them.
            else:
                count += 2
    return count