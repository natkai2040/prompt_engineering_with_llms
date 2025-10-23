def frequency_lists(list_of_lists):
    frequency = {}
    for inner_list in list_of_lists:
        for item in inner_list:
            frequency[item] = frequency.get(item, 0) + 1
    return frequency