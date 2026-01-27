# Renamed a file

with open("old.txt") as f:
    content = f.read()

with open("new.txt", "w") as f1:
    f1.write(content)