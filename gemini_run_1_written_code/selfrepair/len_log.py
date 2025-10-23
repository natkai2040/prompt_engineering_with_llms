def len_log(sentence):
    words = sentence.split() # Splits the sentence into words, handling multiple spaces and stripping leading/trailing whitespace.
    
    if not words: # Check if the list of words is empty (e.g., for empty string or only spaces).
        return 0 # If no words, the length of the longest word is 0.
        
    # Use a generator expression with max() to find the longest word's length.
    # This is safe now because we've ensured 'words' is not empty.
    return max(len(word) for word in words)