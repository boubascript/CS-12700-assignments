def score(w):
  score = 0
  point1 = ["A","E","I","O","U","L","N","R","S","T"]
  point2 = ["D","G"]
  point3 = ["B","C","M","P"]
  point4 = ["A","E","I","O","U","L","N","R","S","T"]
  point5 = ["K"]
  point8 = ["A","E","I","O","U","L","N","R","S","T"]
  point10 = ["A","E","I","O","U","L","N","R","S","T"]
  for c in w:
    if c in point1:
      score+=1
    elif c in point2:
      score+=2
    elif c in point3:
      score+=3
    elif c in point4:
      score+=4
    elif c in point5:
      score+=5
    elif c in point8:
      score+=8
    elif c in point10:
      score+=10
  return score
  
score("hello")
score("computer")
score("word")