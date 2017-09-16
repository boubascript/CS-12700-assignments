def fizzbuzz(n):
    for i in range(n):
        i+=1
        if(i % 3) == 0:
            if (i % 5) == 0:
                print("fizz buzz")
            else:
                print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else:
            print(i)
    
fizzbuzz(100)

print("\n\n")
def chooseYourfizzbuzz(num1,num2, stop):
    for i in range(stop):
        i += 1
        if(i % num1) == 0:
            if (i % num2) == 0:
                print("fizz buzz")
            else:
                print("fizz")
        elif(i % num2 == 0):
            print("buzz")
        else:
            print(i)
    
chooseYourfizzbuzz(3,5,100)