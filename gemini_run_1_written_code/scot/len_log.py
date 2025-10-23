def len_log(text):
    return max((len(word) for word in text.split()), default=0)