# Replace specific words in a text file with asterisks

with open ("d.txt") as f:
    data = f.read()
    if ("Donkey") in data:
        b = data.replace("Donkey", "#######")
    with open ("d.txt", "w") as f2:
        f2.write(b)
