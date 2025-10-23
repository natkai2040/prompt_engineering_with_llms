def multiply_num(numbers):
    # Get the length of the input list/tuple
    length = len(numbers)

    # Handle the edge case of an empty list to prevent division by zero
    if length == 0:
        raise ValueError("Input list cannot be empty. Division by zero is not allowed.")

    # Initialize product to 1 (multiplicative identity)
    product = 1

    # Multiply all numbers in the list
    for num in numbers:
        product *= num

    # Divide the product by the length of the list
    return product / length