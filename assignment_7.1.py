fname = input("Enter File Name")
fhandle = open(fname)
for line in fhandle:
    line = line.rstrip()
    print(line.upper())
