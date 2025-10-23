def Find_Min_Length(list_of_sublists):
    if not list_of_sublists:
        return float('inf') # Or 0, depending on specific requirements for empty input. float('inf') is standard for min of empty set.
    
    lengths = [len(sublist) for sublist in list_of_sublists]
    return min(lengths)