def multiply_num(numbers):
    product_value = 1.0
    list_length = len(numbers)

    if list_length == 0:
        return 0.0

    for num in numbers:
        product_value *= num

    return product_value / list_length