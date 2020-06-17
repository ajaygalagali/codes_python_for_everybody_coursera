import urllib.error,urllib.request,urllib.parse
import re
fhand = urllib.request.urlopen('https://www.quora.com')

numList = list()
for line in fhand:
    tempList = re.findall('https://(w.+")+',line.decode())
    if tempList.__sizeof__() < 1:
        continue
    for i in tempList:
        numList.append(i)
for i in numList:
    print(i)

