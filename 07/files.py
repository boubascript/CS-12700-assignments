#readlines() keeps \n at end of string
#grab a book and other files and mess with files
#use them to build frequency

# You can read a file into a big string using read
f = open("data.dat")
# f is now a file object and we can read from it
s = f.read()
f.close()
print(s)

# we can do the same thing by chaining read onto the open
s2 = open("data.dat").read()
print(s2)


# once it's a tring we can do things with it
# by default split splits on whitespace
s3 = open("data.dat").read()
l = s3.split()
print(l)

# once it's a tring we can do things with it
# here we split on newline
s3 = open("data.dat").read()
l = s3.split("\n")
print(l)

# if we want to split on lines, we can use readlines()
l2 = open("data.dat").readlines()
print(l2)

# or we can read one line at a time with readline()
f = open("data.dat")
for line in f:
    print(line)

# or just go back to read to use a char at a time
s = open("data.dat").read()
for c in s:
    print(c)