# string_times (prob/p193507)
def string_times(str, n):
  return str *n

#front_times (prob/p165097)
def front_times(str, n):
  return str[0:3] * n

#string_bits (prob/p113152)
def string_bits(str):
  bits = ""
  i = 0
  for l in str:
    if (i % 2 == 0):
      bits += l
    i +=1 
  return bits

#lone_sum (prob/p143951)
def lone_sum(a, b, c):
  if (a==b and b==c and a==c):
    return  0
  elif (b==c):
    return a 
  elif(a == c):
      return b 
  elif (a==b) :
    return c
  else:
    return a + b + c

#string_splosion (prob/p118366)
def string_splosion(str):
  splosion = ""
  for i in range(len(str)+1):
    splosion += str[0:i]
  return splosion

#cigar_party (prob/p195669)
def cigar_party(cigars, is_weekend):
  return cigars >= 40 and ( is_weekend or cigars <= 60)

