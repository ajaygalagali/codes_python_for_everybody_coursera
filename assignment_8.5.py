fname = input("Enter File Name")
fhandle = open(fname)
lineSplit = list()
count = 0
for line in fhandle:
    if line.startswith('From'):

        lineSplit = line.split(": ")
        # print(line)
        # print(lineSplit)
        try:
            print(lineSplit[1].strip())
            count+=1
        except:
            pass
print("There were", count, "lines in the file with From as the first word")
