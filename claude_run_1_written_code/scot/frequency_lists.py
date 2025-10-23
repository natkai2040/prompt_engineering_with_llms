def frequency_lists(lists):
    if not lists:
        return {}
    
    frequency = {}
    
    for lst in lists:
        lst_tuple = tuple(lst)
        if lst_tuple in frequency:
            frequency[lst_tuple] += 1
        else:
            frequency[lst_tuple] = 1
    
    return frequency