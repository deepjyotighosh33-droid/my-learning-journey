def rem(l, word):
    for item in l:
        l.remove(word)
        return l
    
l = ["DJ", "Harry", "Carry"]

print(rem(l, "Carry"))
