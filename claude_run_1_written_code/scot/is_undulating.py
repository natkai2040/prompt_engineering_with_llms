def is_undulating(n):
    s = str(n)
    
    if len(s) < 3:
        return False
    
    if s[0] == s[1]:
        return False
    
    digit1 = s[0]
    digit2 = s[1]
    
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] != digit1:
                return False
        else:
            if s[i] != digit2:
                return False
    
    return True