data = [
  [1,1,2],
  [2,2,0.5],
  [-1,-3,2],
  [5,2,1]
  ]

def getMin(xy):
  mymin = data[0][xy] - data[0][2]
  for circ in data:
    if(circ[xy] - circ[2] < mymin):
      mymin = circ[xy]-circ[2]
  return mymin

def getMax(xy):
  mymax = data[0][xy] + data[0][2]
  for circ in data:
    if (circ[xy] + circ[2] > mymax):
      mymax = circ[xy]+circ[2]
  return mymax
  
def bounding_rect(data):
  minX = getMin(0)
  minY = getMin(1)
  maxX = getMax(0)
  maxY = getMax(1)
  return [(minX,minY),
  (minX,maxY),
  (maxX,maxY),
  (maxX,minY)]

print("Bounding Rectangle Coordinates:")
print(bounding_rect(data))