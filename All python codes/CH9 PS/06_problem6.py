# Replace specific words in a text file with asterisks

words = ["Donkey", "badass"]

with open ("d.txt", "r") as f:
    contNew = f.read()

    for w in words:
        contNew = contNew.replace(w, "#" * len(w))

    with open ("d.txt", "w") as f2:
        f2.write(contNew)
        print("Done")