def find_substring(list_of_strings, substring):
  """
  Checks if a substring is present in any of the strings within a given list.

  Args:
    list_of_strings: A list of string values to search within.
    substring: The substring to search for.

  Returns:
    True if the substring is found in any string in the list, False otherwise.
  """
  for s in list_of_strings:
    if substring in s:
      return True
  return False