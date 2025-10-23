def decimal_to_binary(decimal_num):
    if decimal_num == 0:
        return "0"

    binary_str_reversed = []
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_str_reversed.append(str(remainder))
        decimal_num //= 2
    return "".join(binary_str_reversed[::-1])