def is_undulating(number):
    s = str(number)
    n = len(s)

    # A number must have at least two digits to be undulating.
    # For example, '5' cannot be undulating.
    if n < 2:
        return False

    # The first two digits must be different for an undulating pattern (e.g., A B A B...).
    # If they are the same (e.g., '11', '777'), it's not undulating.
    if s[0] == s[1]:
        return False

    # Check the remaining digits for the alternating pattern.
    # s[i] should be s[0] if i is even (0-indexed: 0, 2, 4,...)
    # s[i] should be s[1] if i is odd (0-indexed: 1, 3, 5,...)
    # We already checked s[0] and s[1], so start from s[2].
    for i in range(2, n):
        if i % 2 == 0:  # Even index, should match the first digit
            if s[i] != s[0]:
                return False
        else:  # Odd index, should match the second digit
            if s[i] != s[1]:
                return False

    # If all checks pass, the number is undulating.
    return True