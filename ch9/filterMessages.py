def filter_messages(messages):
    curse_words = []
    count_words = []
    for i in messages:
        words = []
        words = messages.split()
        new_words = [] 
        bad_words = []
        print(words)
        if "dang" in messages:
            messages.join(bad_words)
        print(words)
