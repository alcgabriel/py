def filter_messages(messages):
    filtered_msg = []
    filtered_count = []
    
    for i in messages:
        good_words = []
        dang_words = []
        words = i.split()
        #print(words)
        for word in words:
            # print(word)
            if word == "dang":
             #   print(word, 'bad')
                dang_words.append(word)
               # print(dang_words, "badlist")
               # dang_words.append(dang_words)
            
            else:
               
                good_words.append(word)
                sentence = " ".join(good_words)
        filtered_msg.append(sentence)
        
            #print(good_words, 'goodlist')
           # print(sentence)
        filtered_count.append(len(dang_words))
    
   # print(filtered_count)
    return filtered_msg, filtered_count
