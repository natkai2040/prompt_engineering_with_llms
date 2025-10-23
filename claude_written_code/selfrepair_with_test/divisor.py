def divisor(n):
    count = 0
    # Iterate from 1 up to n (inclusive)
    for i in range(1, n + 1):
        # If i divides n evenly, it's a divisor
        if n % i == 0:
            count += 1
    return count