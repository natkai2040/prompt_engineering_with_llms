def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_digits = []
    # Use a temporary variable to avoid modifying the original input if it were needed elsewhere,
    # or just use decimal_num directly.
    current_num = decimal_num

    while current_num > 0:
        remainder = current_num % 2
        binary_digits.append(str(remainder))
        current_num = current_num // 2

    # The digits are collected in reverse order (least significant first),
    # so we reverse the list and then join them to form the final string.
    return "".join(binary_digits[::-1])