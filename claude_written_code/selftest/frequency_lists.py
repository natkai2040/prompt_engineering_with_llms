def frequency_lists(lists):
    freq = {}
    for sublist in lists:
        for element in sublist:
            freq[element] = freq.get(element, 0) + 1
    return freq