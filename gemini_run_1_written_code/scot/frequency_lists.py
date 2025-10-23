import collections

def frequency_lists(list_of_lists):
    """
    Calculates the frequency count of each unique sub-list within a list of lists.
    Since lists are unhashable, they are converted to tuples to be used as dictionary keys.

    Args:
        list_of_lists: A list where each element is itself a list (e.g., [[1,2], [3], [1,2]]).

    Returns:
        A collections.Counter object (which acts like a dict) where keys are tuples
        (representing the original sub-lists) and values are their frequencies.

    Examples:
        >>> frequency_lists([[1, 2], [3], [1, 2], [4, 5], [3]])
        Counter({(1, 2): 2, (3,): 2, (4, 5): 1})
        >>> frequency_lists([['a'], ['b', 'c'], ['a'], ['b', 'c']])
        Counter({('a',): 2, ('b', 'c'): 2})
        >>> frequency_lists([])
        Counter()
    """
    # Convert each inner list to a tuple to make it hashable
    tuple_representations = [tuple(sublist) for sublist in list_of_lists]

    # Use collections.Counter to efficiently count frequencies of these tuples
    frequency_counts = collections.Counter(tuple_representations)

    return frequency_counts