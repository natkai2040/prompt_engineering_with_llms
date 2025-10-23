def frequency_lists(list_of_lists):
    frequency_map = {}
    for sublist in list_of_lists:
        for item in sublist:
            frequency_map[item] = frequency_map.get(item, 0) + 1
    return frequency_map