def len_log(word_list):
    max_length = 0
    for word in word_list:
        current_word_length = len(word)
        if current_word_length > max_length:
            max_length = current_word_length
    return max_length