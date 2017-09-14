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

