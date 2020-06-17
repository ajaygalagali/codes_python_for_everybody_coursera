fname = input("Enter file name: ")
fhandle = open(fname)
words  = list()
temp = list()
for line in fhandle:
    temp = line.split()
    for word in temp:
        if not word in words:
            words.append(word)

words.sort()
print(words)