def power(a, b):
    # Any number to the power of 0 is 1
    if b == 0:
        return 1

    result = 1
    # Multiply 'a' by itself 'b' times
    for _ in range(b):
        result *= a
    return result