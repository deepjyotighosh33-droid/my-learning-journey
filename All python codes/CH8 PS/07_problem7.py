#remove all occurrences of a given word from a list of strings

def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
l = ["DJ", "Harry", "Rohan", "an"]

print(rem(l, "an"))
