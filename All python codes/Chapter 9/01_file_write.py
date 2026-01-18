st = "DJ you are amazing"

f = open("myfile.txt", "w") # if given a in place of w then it will append the data to the existing file

f.write(st)

f.close()