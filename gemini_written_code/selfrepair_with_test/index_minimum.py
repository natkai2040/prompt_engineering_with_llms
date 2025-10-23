def index_minimum(data_tuples):
    # Use the min function with a lambda key to find the tuple
    # that has the minimum value at its second position (index 1).
    # The key function `lambda x: x[1]` tells min to compare elements
    # based on their second item.
    min_value_record = min(data_tuples, key=lambda x: x[1])
    
    # The problem asks for the name associated with this minimum value.
    # The name is the first element (index 0) of the identified tuple.
    return min_value_record[0]