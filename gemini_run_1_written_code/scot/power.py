def power(a, b):
    if b == 0:
        return 1

    result = 1.0
    abs_b = abs(b)

    for _ in range(abs_b):
        result *= a

    if b < 0:
        return 1 / result
    else:
        return result