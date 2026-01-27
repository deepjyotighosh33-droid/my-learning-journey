# Find if the word "Python" exists in a text file. If it does, print "Yup found it", else print "Not found".

with open("log.txt") as f:
    content = f.read()
    if("Python") in content:
        print("Yup found it")
    else:
        print("Not found")

