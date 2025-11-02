# Spam filtre comment checker

p1 = "Welcome"
p2 = "Raw"
p3 = "Hero"
p4 = "love"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("Spam comment detected")
else:
    print("Not spam")    
