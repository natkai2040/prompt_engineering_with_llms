def index_minimum(tuples_list):
    if not tuples_list:
        return None
    return tuple(min(values) for values in zip(*tuples_list))