def fizzbuzz(n):
    for i in range(n):
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