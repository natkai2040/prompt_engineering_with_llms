def index_minimum(records):
    # The min() function with a custom key can efficiently find the tuple
    # whose second element (the value) is the smallest.
    # The lambda function `lambda x: x[1]` specifies that for each tuple `x`
    # in `records`, its second element should be used for comparison.
    min_record = min(records, key=lambda x: x[1])

    # Once the tuple with the minimum value is found, return its first element
    # which is the name.
    return min_record[0]