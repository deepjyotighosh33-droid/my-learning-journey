f = open("poems.txt")

a = f.read()

if ("twinkle" in a):
    print("Yes, 'twinkle' is present")
else:
    print("No, 'twinkle' is not present")

f.close()