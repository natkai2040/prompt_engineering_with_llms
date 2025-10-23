def find_substring(strings, substring):
    for string in strings:
        if substring in string:
            return True
    return False