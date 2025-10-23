import collections

def frequency_lists(list_of_lists):
    """
    Calculates the frequency count of inner lists within a list of lists.

    Args:
        list_of_of_lists: A list where each element is itself a list.

    Returns:
        A dictionary where keys are tuple representations of the inner lists
        and values are their respective frequencies.
    """
    counts = collections.defaultdict(int)
    for sublist in list_of_lists:
        # Lists are not hashable, so they cannot be used directly as dictionary keys.
        # Convert each sublist to a tuple, which is immutable and hashable.
        counts[tuple(sublist)] += 1
    return dict(counts)
