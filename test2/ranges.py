import random

def build_rangelist(length=10):
  l=[]
  lowval = 5
  
  for i in range(length):
    r = [lowval, lowval+random.randrange(1,20)]
    l.append(r)
    lowval = r[1] + random.randrange(1,20)
  return l
  
rangelist = build_rangelist()

def overlap(t1,t2):
  return t2[0] < t1[1]

def merge(t1,t2):
  merged = []
  if t1[0] < t2[0]:
    merged.append(t1[0])
  else:
    merged.append(t2[0])
  if t2[1] > t1[1]:
    merged.append(t2[1])
  else:
    merged.append(t1[1])
  return merged
  
def add_range(rangelist,newrange):
  for i in range(len(rangelist)):
    if newrange[0] < rangelist[i][0]:
      rangelist.insert(i,newrange)
  return rangelist
  
rangelist = build_rangelist()
print(rangelist)
print(overlap(rangelist[0],rangelist[0]))
print(merge(rangelist[0],rangelist[0]))
print(add_range(rangelist[0],rangelist[0]))
      
  
  
  
  
