import csv

# method 1 - use split
# f  = open("sample.csv")
# for line in f.readlines():
#     line = line.strip()
#     l  = line.split(",")
#     print(l)
#     f.close()

# use the CSV library to convert csv --> lists
f = open("sample.csv")
csv_reader = csv.reader(f)
l = []
for line in csv_reader:
    l.append(line)
f.close()
print(l)
emails = [ x[2] for x in l]
print(emails)


print("\n-------------------------------------------\n")

# process CSV --> Dict
l=[]
f = open("sample.csv")
csv_dict_reader = csv.DictReader(f)
for line in csv_dict_reader:
    l.append(line)
f.close()

emails = [d['email'] for d in l]

print(emails)
