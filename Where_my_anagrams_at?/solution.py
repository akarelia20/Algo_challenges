def anagrams(word,words):
    result = []
    word_dict= {} #saves letter-occurances of the word in a dict(key-value pairs)
    for i in word:
        if i not in word_dict:
            word_dict[i] = 1
        else:
            word_dict[i] +=1
    # itrate through the list of words
    for word in words:
        words_dict ={}
        #itrating through letters in each word and storing the occrance in dict
        for j in word:
            if j not in words_dict:
                words_dict[j] = 1
            else:
                words_dict[j] +=1
        # comparing the two dict; dictonary of given word vs a word in a list
        if word_dict == words_dict:
            #if the both dictonaries are same append the word (present in a list) to result list.
            result.append(word) 
    return result
