def index_minimum(tuples):
    """
    Extracts the lexicographically minimum value record from a given tuple of tuples.

    Args:
        tuples: A tuple of tuples, where each inner tuple represents a record.

    Returns:
        The minimum record (an inner tuple) based on lexicographical comparison,
        or None if the input tuple is empty.
    """
    if not tuples:
        return None
    return min(tuples)