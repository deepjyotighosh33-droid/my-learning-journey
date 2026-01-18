f = open("file.txt")

lines = f.readlines()

print(lines, type(lines))

f.close()


'''
line = f.readlines()
while(line != ""):
    print(line)
    line = f.readlines()

f.close()
'''