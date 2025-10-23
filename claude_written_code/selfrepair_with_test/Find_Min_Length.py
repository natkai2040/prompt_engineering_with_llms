def Find_Min_Length(list_of_lists):
    if not list_of_lists:
        # If the input list of lists is empty, there are no sublists to measure.
        # Returning 0 is a common convention for minimum length when nothing is present.
        return 0
    
    # Use a generator expression to get the length of each sublist,
    # then find the minimum among these lengths. This is efficient
    # as it doesn't create an intermediate list of all lengths.
    return min(len(sublist) for sublist in list_of_lists)