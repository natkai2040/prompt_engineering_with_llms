def index_minimum(tuples):
    if not tuples:
        return None
    
    min_tuple = min(tuples, key=lambda t: min(t))
    min_index = tuples.index(min_tuple)
    
    return (min_index, min_tuple)