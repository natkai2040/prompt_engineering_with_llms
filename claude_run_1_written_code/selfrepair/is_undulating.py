def is_undulating(n):
    s = str(n)
    if len(s) < 3:
        return False
    
    if len(set(s)) != 2:
        return False
    
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    
    return True
