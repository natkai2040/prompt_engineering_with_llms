def frequency_lists(list_of_lists):
    from collections import Counter
    freq = Counter(tuple(sublist) for sublist in list_of_lists)
    return dict(freq)