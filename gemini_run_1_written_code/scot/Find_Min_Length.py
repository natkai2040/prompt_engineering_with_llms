def Find_Min_Length(input_list):
    min_length = float('inf')
    found_sublist = False

    for item in input_list:
        if isinstance(item, list):
            found_sublist = True
            current_length = len(item)
            min_length = min(min_length, current_length)
    
    if found_sublist:
        return min_length
    else:
        return None