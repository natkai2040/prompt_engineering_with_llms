def find_substring(list_of_strings, substring):
    for item_string in list_of_strings:
        if substring in item_string:
            return True
    return False