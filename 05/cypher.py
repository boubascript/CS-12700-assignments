#My own Helper Functions--------

def isLower(c):
    return ord(c)>= 97 and ord(c) <= 122

def isUpper(c):
    return ord(c) >= 65 and ord(c) <= 90

def shift(c,r,lowbd, highbd):
    newAscii = ord(c) + r
    if(newAscii > highbd):
        newAscii = lowbd + ((newAscii- highbd - 1) % 26) 
    return chr(newAscii)

#Assigned helper functions/routines
def encode_letter(c,r):
    if(isLower(c)):
        return(shift(c,r,97,122))
    elif(isUpper(c)):
        return(shift(c,r,65,90))
    else:
        return c
 
def encode_string(s,r):
    words = s.split()
    newString = []
    for word in words:
        new_Word = ""
        for ltr in word:
            ltr = encode_letter(ltr,r)
            new_Word += ltr
        newString.append(new_Word)
    return (" ".join(newString))
        
def full_encode(s):
    result = ""
    for r in range(26):
        result += encode_string(s,r) + "\n"
    return result

def file_encode(file,r):
    result = ""
    try:
        with open(file) as f:
            msg = f.read()
            msgWords = msg.split("\n")
            for line in msgWords:
                line = encode_string(line,r)
                result += line + "\n"
    except FileNotFoundError:
        print("Error: This file doesn't exist! Try again.")
        print("Hint: Use path cyphertest.txt for now")
    return result

def full_file_encode(file):
    return full_encode(file_encode(file,0))
    
print(full_encode("Alert: This message encrypted with a weak cypher!"))

print(full_file_encode("cyphertest.txt"))