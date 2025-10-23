def multiply_num(numbers_list):
    product = 1
    for num in numbers_list:
        product *= num
    
    list_length = len(numbers_list)
    
    if list_length == 0:
        return 0
    else:
        return product / list_length