def encode(s):
  encoded = []
  count = 1
  for i in range(len(s)-1):
    if (s[i] == s[i+1]):
      count+=1
      if(i+2 == len(s)):
        if(count==1):
          encoded.append(s[i])
        else:
          encoded.append(count)
          encoded.append(s[i])
    else:
      if(count==1):
        encoded.append(s[i])
      else:
        encoded.append(count)
        encoded.append(s[i])
      count = 1
  return encoded
    

    
print(encode("bbaaa"))
print(encode("aabcccdeeeeaaa"))
print(encode("aaaaa"))
print(encode("abcdefggghh"))
print(encode("xxyyzz"))
