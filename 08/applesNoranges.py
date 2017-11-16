
st = "7 11"
ab = "5 15"
mn = "3 2"
apples = [-2 ,2 ,1]
oranges = [5 ,-6]

s,t = st.strip().split(' ')
s,t = [int(s),int(t)]
a,b = ab.strip().split(' ')
a,b = [int(a),int(b)]
m,n = mn.strip().split(' ')
m,n = [int(m),int(n)]
#apples = [int(apple_temp) for apple_temp in input.strip().split(' ')]
#oranges = [int(orange_temp) for orange_temp in input.strip().split(' ')]

def onHouse(n):
    return n >= s and n <= t

def applesOnHouse():
    sum = 0
    for d in apples:
        if(onHouse(a + d)):
            sum +=1
    return sum

def orangesOnHouse():
    sum = 0
    for d in oranges:
        if(onHouse(b + d)):
            sum +=1
    return sum

print(applesOnHouse())
print(orangesOnHouse())