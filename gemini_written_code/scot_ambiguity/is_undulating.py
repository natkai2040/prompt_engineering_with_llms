def is_undulating(s: str) -> bool:
    # An undulating number needs at least 3 digits to show an 'ABA' pattern.
    # For example, '', '1', '12', '11' are not considered undulating as they don't
    # establish a clear alternating sequence of two numbers.
    if len(s) < 3:
        return False

    # The first two characters establish the alternating pattern.
    # s[0] is expected at even indices (0, 2, 4, ...)
    # s[1] is expected at odd indices (1, 3, 5, ...)
    char0 = s[0]
    char1 = s[1]

    # Iterate from the third character (index 2) to the end of the string
    for i in range(2, len(s)):
        if i % 2 == 0:  # If the current index is even
            if s[i] != char0: # It must match the character at index 0
                return False
        else:  # If the current index is odd
            if s[i] != char1: # It must match the character at index 1
                return False

    # If the loop completes without returning False, all characters followed the pattern.
    return True