
def freq(n,l):
    count = 0
    for num in l:
        if num == n:
            count += 1
    return count

#print(freq(3,[3,2,2,1,3,4,5,4,3,4,3]))

def min(l):
    min = l[0]
    for i in range(1,len(l)):
        if l[i] < min:
            min = l[i]
    return min

#helper function for mode
def max(l):
    max = l[0]
    for i in range(1,len(l)):
        if l[i] > max:
            max = l[i]
    return max

def mode(l):
    counts = []
    numbers = []
    numbers.append(l[0])
    counts.append(0)
    for num in l:
        if num in numbers:
            counts[numbers.index(num)] += 1
        else:
            numbers.append(num)
            counts.append(1)
    #print(numbers)
    #print(counts)
    return numbers[counts.index(max(counts))]

#print(mode([3,2,2,1,3,4,5,4,3,4,3]))