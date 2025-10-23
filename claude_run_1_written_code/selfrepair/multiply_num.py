def multiply_num(numbers):
    if not numbers:
        return 0
    product = 1
    for num in numbers:
        product *= num
    return product / len(numbers)