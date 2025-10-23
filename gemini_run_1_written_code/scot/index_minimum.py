def index_minimum(data_tuples, index_to_compare):
    """
    Extracts the record (tuple) from a list of tuples that has the minimum value
    at a specified index.

    Args:
        data_tuples (list): A list of tuples. Each tuple is assumed to have at least
                            `index_to_compare + 1` elements.
        index_to_compare (int): The index within each tuple to use for comparison.

    Returns:
        tuple: The tuple from `data_tuples` that has the minimum value at
               `index_to_compare`. Returns `None` if `data_tuples` is empty.
               If multiple tuples have the same minimum value, the first one encountered
               is returned.
    """
    if not data_tuples:
        return None

    # Use the min function with a lambda key to compare tuples based on the value
    # at the specified index.
    min_record = min(data_tuples, key=lambda record: record[index_to_compare])
    
    return min_record