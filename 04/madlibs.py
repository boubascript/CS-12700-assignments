import random 

story = """ There once was a NOUN who VERB. He was very ADJECTIVE. He VERB very well.   """
nouns = [ "chair",  "head", "desk", "table", "tree", "paper", "towel","file" ]
verbs = [ "kill" , "coded" , "ran" , "jumping", "swim" , "watch" , "existed"]
adjectives = [ "loud" , "ugly" , "beautiful" , "green","old"]
keywords = ["NOUN" , "VERB" , "ADJECTIVE" , "PRONOUN"]


def madlibs():
    global story
    s = story.strip()
    words = s.split(" ")
    
    for word in words:
        if word == "NOUN":
            pass
        elif word == "VERB":
            pass
        elif word == "ADJECTIVE":
            pass
        elif word == "PRONOUN":
            pass
            