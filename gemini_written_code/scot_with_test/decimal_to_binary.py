def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return '0'

    binary_digits = []
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_digits.append(str(remainder))
        decimal_num = decimal_num // 2

    # The digits are collected in reverse order, so we need to reverse the list
    # and then join them to form the final binary string.
    binary_digits.reverse()
    return ''.join(binary_digits)