import random
import re

story = """ There once was a NOUN who VERB. He was very ADJECTIVE. He VERB very well.   """
nouns = ["chair", "head", "desk", "table", "tree", "paper", "towel", "file"]
verbs = ["kill", "coded", "ran", "jumping", "swim", "watch", "existed"]
adjectives = ["loud", "ugly", "beautiful", "green", "old"]
keywords = ["NOUN", "VERB", "ADJECTIVE"]


def convert(word):
    global nouns, verbs, adjectives
    if "NOUN" == word:
        return random.choice(nouns)
    elif "VERB" == word:
        return random.choice(verbs)
    elif "ADJECTIVE" == word:
        return random.choice(adjectives)
    else:
        return word


def madlibs():
    global story
    # Prepare for search
    orig = story.strip()

    # Search for the words to replace
    # Returns match objects which we inspect
    matches = re.finditer(r'NOUN|VERB|ADJECTIVE', orig)

    # Start of unmatched section we're working on
    start = 0

    # Final string
    s = ""

    for x in matches:
        span = x.span()  # Tuple with the start and end indexes of the match
        new = convert(orig[span[0]:span[1]])  # Convert match to the proper random word
        s += orig[start:span[0]] + new  # Add the section we skipped and the replaced word to the ending string
        start = span[1]  # Mark the end of this match as the beginning of the next skipped section
    s += orig[start:]  # Add any remaining bits of the string

    return s  # return said string
    orig = story.strip()

    result = re.finditer(r'NOUN|VERB|ADJECTIVE', orig)

    s = ""

    for x in result:
        span = x.span()
        new = convert(orig[span[0]:span[1]])
        s = orig[0:span[0]] + new + orig[span[1]:]

    return s

if __name__ == "__main__":
    print(madlibs())
            