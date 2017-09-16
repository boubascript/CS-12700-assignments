punct = [".",",","?","!",":",";",""]
def piglatinify(s):
    s = s.split(" ")
    translated = ""
    for word in s:
        if(len(word) > 1 and word[:1] not in ["a","A","E","e","i","I","O","o","u","u"]):
            word = word[1:] + word[:1] + "ay"
        elif (word not in punct):
           word = word + "ay"
        i = 0
        for ltr in word:
            if ltr in punct:
                punc = word[i]
                p
                shifted = word.replace(punc,"",1)
                shifted += punc
                print(">>>>>" + shifted)
            i += 1
        
        translated += word + " "
    print(translated)
        
    
           
piglatinify(""" Hello... This is pig latin my guy. We lit!! """)

        
