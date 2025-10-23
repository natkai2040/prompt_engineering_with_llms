def Find_Min_Length(list_of_lists):
    # Handle the edge case where the input list of lists is empty.
    # In this scenario, there are no sublists to measure, so we return
    # float('inf') to indicate that no finite minimum length was found.
    if not list_of_lists:
        return float('inf')

    # Initialize min_length to a value larger than any possible sublist length.
    # float('inf') is suitable as it ensures the length of the very first
    # sublist processed will always be smaller, correctly setting the initial minimum.
    min_length = float('inf')

    # Iterate through each sublist in the provided list_of_lists.
    for sublist in list_of_lists:
        # Calculate the length of the current sublist.
        current_length = len(sublist)
        
        # If the current sublist's length is less than the smallest length
        # found so far, update min_length.
        if current_length < min_length:
            min_length = current_length
            
    # After checking all sublists, min_length will hold the smallest length found.
    return min_length