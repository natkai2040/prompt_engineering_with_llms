def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = []
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    
    # Repair: Reverse the list of digits before joining them
    return "".join(binary_digits[::-1])