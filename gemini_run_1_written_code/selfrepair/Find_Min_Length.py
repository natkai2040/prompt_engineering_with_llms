def Find_Min_Length(list_of_lists):
    min_length = float('inf')
    
    for sublist in list_of_lists:
        min_length = min(min_length, len(sublist))
            
    return min_length