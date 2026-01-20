with open("log.txt") as f:
    content = f.read()
    if("Python") in content:
        print("Yup found it")
    else:
        print("Not found")

