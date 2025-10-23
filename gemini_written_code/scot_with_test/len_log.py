def len_log(words_list):
    if not words_list:
        return 0

    max_length = 0
    for word in words_list:
        current_word_length = len(word)
        if current_word_length > max_length:
            max_length = current_word_length
    return max_length