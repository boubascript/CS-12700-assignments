import math
alphabet = {'a':0 , "b":0, "c":0 , "d":0, "e": 0 , "f":0 , "g":0 , "h":0,
            "i":0 , "j":0 , "k":0 , "l":0 , "m":0 , "n":0 , "o":0 , "p":0 , "q":0 , "r":0,
            "s":0 , "t":0 , "u":0 , "v":0 , "w":0 , "x":0 , "y":0 , "z":0 }
alpha = list(alphabet.keys())
#real_stats = [0.08167,0.01492,0.02782,0.04253,0.12702,0.02228,0.02015,0.06094,0.06966,0.00153,0.00772,0.04025,0.02406,0.06749,0.07507,0.01929,0.00095,0.05987,0.06327,0.09056,0.02758,0.00978,0.02360,0.00150,0.01974,0.00074]
puncts = [" ",".",";",":",",","?","!","(",")"]
symbols = ["@","#","$","%","^","&","*","+","-","_","~"]

#create the frequencies that will be compared to as the 'real' values
def create_stats(text):
    total = 0
    try:
        with open(text) as f:
            msg = f.read().lower()
            msgWords = msg.split("\n")
            for line in msgWords:
                notcount = 0
                for c in line:
                    if c in puncts or c in symbols:
                        notcount +=1
                total += (len(line) - notcount)
                for key,val in alphabet.items():
                    alphabet[key] = val + line.count(key)
            for key,val in alphabet.items():
                alphabet[key] = val/total
            return list(alphabet.values())
    except FileNotFoundError:
        print("Error: This file doesn't exist! Try again.")
        
# I used hitchikers guide to the galaxy as the text for reference
real_stats = create_stats("hhgttg.txt")

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

""" compare to
    v = newAscii
    v = v - lowbd
    v = (v + r) % 26
    v = v + lowbd
"""

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

#returns smaller of 2 lists
def smaller(l1,l2):
    if(len(l1) > len(l2)):
        return l2
    else:
        return l1
    
def distance(v1,v2):
    sum = 0
    for i in range(len(smaller(v1,v2))):
        sum += (v2[i]-v1[i]) * (v2[i]-v1[i])
    sum = math.sqrt(sum)
    return sum

def build_frequency_vector(s):
    notcount = 0
    for c in s:
        if c in puncts:
            notcount += 1
    total = len(s) - notcount
    v = []
    for l in alpha:
        v.append(s.count(l)/ total)
    return v

def getMin(l):
    min = l[0]
    for i in range(1,len(l)):
        if distances[i] < min:
            min = distances[i]
            min_index = i
    return min
        
def decode(s):
    allrotations = []
    allfrequencies = []
    distances = []
    for i in range(26):
        rstring = encode_string(s,i)
        freq = build_frequency_vector(rstring)
        allrotations.append(rstring)
        allfrequencies.append(freq)
        d = distance(freq,real_stats)
        distances.append(d)
    return allrotations[distances.index(min(distances))]
     

def testcypher():
    #print(real_stats)
    encoded = file_encode("cyphertest.txt",23)
    decoded = decode(encoded)
    print("Encoded: " + encoded)
    print("decoded: " + decoded)
    
testcypher()