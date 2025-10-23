def decimal_to_binary(n):
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return '0'

    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n //= 2
    
    # The digits are collected in reverse order, so reverse the list and join
    return "".join(binary_digits[::-1])