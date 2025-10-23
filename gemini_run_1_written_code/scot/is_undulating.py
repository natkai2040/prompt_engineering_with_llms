def is_undulating(num):
    # Convert the number to a list of integer digits
    s_num = str(num)
    digits = [int(d) for d in s_num]
    n = len(digits)

    # An undulating number requires at least 3 digits to establish the alternating pattern
    # Also handles num=0, which has 1 digit, correctly returning False.
    if n < 3:
        return False

    # Check the relation between the first two digits
    # If they are equal, it cannot be undulating (strict inequality required)
    if digits[0] == digits[1]:
        return False

    # prev_was_less tracks the relation for the previous pair of digits
    # True if digits[k-1] < digits[k], False if digits[k-1] > digits[k]
    prev_was_less = (digits[0] < digits[1])

    # Iterate from the second digit to the second-to-last digit
    # We compare digits[i] and digits[i+1]
    for i in range(1, n - 1):
        d_curr = digits[i]
        d_next = digits[i+1]

        # If adjacent digits are equal, it's not undulating
        if d_curr == d_next:
            return False
        
        # Determine the current relation
        current_is_less = (d_curr < d_next)

        # If the current relation is the same as the previous one,
        # the alternating pattern is broken (e.g., < < or > >)
        if current_is_less == prev_was_less:
            return False
        
        # Update prev_was_less for the next iteration (relation should flip)
        prev_was_less = current_is_less
    
    # If the loop completes, the number is undulating
    return True