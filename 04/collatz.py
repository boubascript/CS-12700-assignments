def collatz(n):
    if (n % 2 == 0):
        n //= 2
    else:
        n = 3*n + 1
    return n

def collatzSequence():
    num = int(input("Enter Number: "))
    print(num)
    while num != 1:
        num = collatz(num)
        print(num)
        
        
collatzSequence()