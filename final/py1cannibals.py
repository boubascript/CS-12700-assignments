data = [21, 9, 5, 8, 10, 13]


def increaseby(data,value):
  count = 0
  for n in data:
    if(n < value):
      count +=1
  return count
  
def canibals(data,target):
  count = 0;
  for n in data:
    if(n > target):
      count +=1
    else:
      if(n + increaseby(data,n) >= target):
        count +=1
  return count
  
print(canibals(data,13))