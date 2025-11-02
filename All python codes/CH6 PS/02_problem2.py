marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40):
    print("Passed")

else:
    print("Failed")