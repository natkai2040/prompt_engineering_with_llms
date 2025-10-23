def is_undulating(s: str) -> bool:
    n = len(s)
    if n < 3:
        return False
    
    for i in range(n - 2):
        if s[i] != s[i+2]:
            return False
    
    return True