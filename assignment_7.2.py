fname = input("Enter File Name :")
fhandle = open(fname)
lineCount = 0
result = float(0)
for line in fhandle:
    if line.startswith("X-DSPAM-Confidence:"):
        lineCount+=1

        result+=float(line[18+1:].strip())
print("Average spam confidence:",result/lineCount)

