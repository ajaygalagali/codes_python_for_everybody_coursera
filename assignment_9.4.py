fname = input("Enter the File Name  :")
fhandle = open(fname)


maxValue = 0
maxKey = ""
words = dict()
for line in fhandle:
    if line.startswith('From '):

        lineSplit = line.split()
        # print(line)
        # print(lineSplit)
        try:
            key = lineSplit[1].strip()
            words[key] = words.get(key,0)+1
        except:
            pass

for k in words:
    if words[k] > maxValue:
        maxValue = words[k]
        maxKey = k

print(maxKey,maxValue)