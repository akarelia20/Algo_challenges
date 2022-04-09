def disemvowel(str):
    vowel = "aeiouAEIOU"
    result = ""
    for i in str:
        isvowel = False
        for j in vowel:
            if i == j:
                isvowel = True
        if isvowel == False:
            result += i
    return result

print(disemvowel("This website is for losers LOL! ")) #Output = Ths wbst s fr lsrs LL! 
