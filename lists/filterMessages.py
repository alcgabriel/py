def filter_messages(messages):
    dang_msg = []
    dang_count = []

    for message in messages:
        good_words = []
        bad_words = []
        words = message.split()
        for i in words: 
            if words == ["dang"]:
                bad_words.append([words[i]])
            
            return words, good_words, bad_words
            dang_count = len(bad_words)
        print(words)

    return dang_msg, dang_count
