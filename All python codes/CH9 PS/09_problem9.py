# Copy the contents of one file to another

with open ("this.txt") as f:
    content = f.read()

with open ("copy.txt", "w") as f1:
    f1.write(content)