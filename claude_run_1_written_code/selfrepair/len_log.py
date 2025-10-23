def len_log(words):
    if isinstance(words, str):
        words = words.split()
    if not words:
        return 0
    return max(len(word) for word in words)