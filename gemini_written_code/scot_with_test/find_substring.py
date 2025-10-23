def find_substring(list_of_string_values, substring):
    for s in list_of_string_values:
        if substring in s:
            return True
    return False