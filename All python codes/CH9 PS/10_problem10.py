# Compare the contents of two files and print whether they are identical or not

with open("this.txt") as f:
    content = f.read()

with open("copy.txt") as f1:
    content2 = f1.read()

if (content == content2):
    print("Files are identical")

else:
    print("Files are not identical")