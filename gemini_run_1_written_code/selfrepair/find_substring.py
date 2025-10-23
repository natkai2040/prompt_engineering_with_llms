def find_substring(substring: str, string_list: list[str]) -> bool:
    """
    Checks if a substring is present in any string within a given list of strings.

    Args:
        substring: The string to search for.
        string_list: A list of strings to search within.

    Returns:
        True if the substring is found in any string in the list, False otherwise.
    """
    return any(substring in s for s in string_list)