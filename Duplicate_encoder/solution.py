def duplicate_encode(word):
    new_word= ""
    word= word.lower()
    dict={} 
    for i in range(0,len(word)): 
        # stored the occurrence of each letter in dict
        if word[i] not in dict:
            dict[word[i]] = 1
        elif word[i] in dict:
            dict[word[i]] += 1
    for i in word:
        if dict[i] > 1:
            new_word += ")"
        else:
            new_word +="("
    return (new_word)