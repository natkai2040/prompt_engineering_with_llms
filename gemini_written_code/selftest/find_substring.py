def find_substring(list_of_strings, substring):
    for s in list_of_strings:
        if substring in s:
            return True
    return False