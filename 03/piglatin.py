punct = [".",",","?","!",":",";",")",""]
vowels = ["a","A","E","e","i","I","O","o","u","u"]

def piglatinify(s):
    s = s.split(" ")
    translated = ""
    for word in s:
        parentheses = False
        if(word[:1] == "("):
            word = word.replace("(","")
            parentheses = True
        if(len(word) > 1 and word[:1] not in vowels):
            word = word[1:] + word[:1] + "ay"
        elif (word not in punct):
           word += "ay"
        puncs = ""
        shifted  = ""
        i = 0
        for ltr in word:
            if ltr in punct:
                punc = word[i]
                puncs += punc
            i += 1
        word = word.replace("".join(puncs),"")
        word += "".join(puncs)
        if(parentheses):
            word = "(" + word
        translated += word + " "
    return translated
        
              
print(piglatinify("""This sentence is in pig latin."""))


def pigLatinTranslator():
    tryagain = True
    while(tryagain):
        try:
            filename = input("Enter file name or path to translate: ")
            with open(filename) as file:
                story = file.read()
                story = story.split("\n")
                for line in story:
                    line = piglatinify(line)
                    print(line)
            print("--------------- \n\n")
            redo = input("Enter to translate another file, type anything to quit.")
            if(redo!= ""):
                tryagain = False
        except FileNotFoundError:
            print("Error: This file doesn't exist! Try again.")
            print("Hint: Use path pigFileTests/piglatintest.txt for now")
            tryagain = True
        
            

pigLatinTranslator()