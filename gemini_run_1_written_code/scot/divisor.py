def divisor(n: int) -> int:
    num = abs(n)

    if num == 0:
        return 0
    if num == 1:
        return 1

    count = 0
    # Iterate up to the square root of num
    # int(num**0.5) converts the float result of sqrt to an integer
    # The +1 ensures that the integer square root itself is included in the range.
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            # If i*i == num, then i is the square root and i and num/i are the same divisor.
            if i * i == num:
                count += 1
            # Otherwise, i and num/i are two distinct divisors.
            else:
                count += 2
    return count