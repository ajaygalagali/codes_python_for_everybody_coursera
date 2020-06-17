import re

fhandle = open("text.txt")
numList = list()
for line in fhandle:
    tempList = re.findall('[0-9]+',line)
    if tempList.__sizeof__() < 1:
        continue
    for i in tempList:
        numList.append(int(i))

print(sum(numList))