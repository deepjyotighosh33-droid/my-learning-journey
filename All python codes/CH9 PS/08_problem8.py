# Find the line number of the first occurrence of the word "Python" in a text file. If the word is not found, print "nope".

with open ("log.txt") as f:
    lines = f.readlines()

lineno =1
for line in lines:
    if("Python" in line):
        print(f"Yup, line no: {lineno}")
        break
    lineno +=1

else:
    print("nope")