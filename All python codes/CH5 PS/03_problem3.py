# SEEING if int and string both as numbers can stay as a string
s = set()

# s.add(18)
# s.add("18") 

n = input("Enter integer: ")
s.add(int(n))
n = input("Enter string: ")
s.add(n)

print(s)