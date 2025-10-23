def is_undulating(s):
    # Numbers with 1 or 2 digits are trivially undulating
    if len(s) < 3:
        return True
    
    # Check the undulating pattern for digits from the third onwards
    # A number is undulating if s[i] == s[i-2] for all i >= 2
    for i in range(2, len(s)):
        if s[i] != s[i-2]:
            return False
            
    # If the loop completes, all digits followed the pattern
    return True