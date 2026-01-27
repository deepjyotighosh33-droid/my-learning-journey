# Write multiplication table of a number to a file

with open("tables.txt", "w") as f:
    a = int(input("Enter a no: "))
    for i in range(1, 11):
        f.write(f"{a} x {i} = {a * i}\n")

print(f"Table of {a} has been written to tables.txt")

