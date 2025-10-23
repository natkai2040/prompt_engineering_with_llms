def decimal_to_binary(n):
    if n >= 0:
        return bin(n)[2:]
    else:
        return '-' + bin(n)[3:]