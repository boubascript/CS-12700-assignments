def collatz(n):
    if (n % 2 == 0):
        n //= 2
    else:
        n = 3*n + 1
    return n

def collatzSequence():
    nan = True
    while(nan):
        try:
            num = int(input("Collatz Sequence \nEnter Number:\n"))
            nan = False
        except ValueError:
            print("Invalid Input! Please enter a number.")
            nan = True
    while num != 1:
        num = collatz(num)
        print(num)
        

collatzSequence()