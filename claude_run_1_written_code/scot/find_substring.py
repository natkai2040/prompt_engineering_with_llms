def find_substring(substring, string_list):
    if not string_list:
        return False
    
    for string in string_list:
        if substring in string:
            return True
    
    return False