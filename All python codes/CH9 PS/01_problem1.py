# Check if the word "twinkle" is present in a text file

f = open("poems.txt")

a = f.read()

if ("twinkle" in a):
    print("Yes, 'twinkle' is present")
else:
    print("No, 'twinkle' is not present")

f.close()