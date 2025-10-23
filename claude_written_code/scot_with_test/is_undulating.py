def is_undulating(s: str) -> bool:
    # 1. Check minimum length
    if len(s) < 3:
        return False

    # 2. Identify the two potential alternating digits
    char_d1 = s[0]  # Expected character for even indices
    char_d2 = s[1]  # Expected character for odd indices

    # 3. Check if the two initial digits are distinct
    if char_d1 == char_d2:
        return False

    # 4. Iterate and verify the alternating pattern from index 2 onwards
    for i in range(2, len(s)):
        if i % 2 == 0:  # Current index is even
            if s[i] != char_d1:
                return False
        else:  # Current index is odd
            if s[i] != char_d2:
                return False

    # 5. If the loop completes, all conditions are met
    return True