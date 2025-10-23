from collections import Counter

def frequency_lists(list_of_lists):
    # Step 3: Flatten the list of lists into a single iterable of all elements.
    # A generator expression is used for memory efficiency.
    all_elements = (item for sublist in list_of_lists for item in sublist)

    # Step 4: Use collections.Counter to get the frequency of each element.
    frequencies_counter = Counter(all_elements)

    # Step 5 & 6: Convert the Counter object to a standard dictionary and return it.
    return dict(frequencies_counter)