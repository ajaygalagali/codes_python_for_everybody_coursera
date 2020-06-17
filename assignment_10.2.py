fname = input("Enter File Name :")

fhandle = open(fname)
firstSplit = []
secondSpilt =[]
d = dict()
for line in fhandle:
    if line.startswith("From "):
        firstSplit = line.strip().split()
        secondSpilt = firstSplit[5].split(":")
        d[secondSpilt[0]] = d.get(secondSpilt[0],0)+1

s = sorted(d)

for i in s:
    print(i,d[i])


