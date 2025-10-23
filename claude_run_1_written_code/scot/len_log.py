def len_log(words):
    if not words:
        return 0
    
    if isinstance(words, str):
        words = words.split()
    
    if not words:
        return 0
    
    longest_word = max(words, key=len)
    return len(longest_word)