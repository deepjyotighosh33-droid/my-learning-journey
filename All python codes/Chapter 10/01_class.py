class Employee:
    language = "Py" # class attribute
    salary = 120000

DJ = Employee()
DJ.name = "DJ" #instance attribute
print(DJ.name, DJ.language, DJ.salary)

Harry = Employee()
Harry.name = "Harry" #instance attribute
print(Harry.name, Harry.language, Harry.salary)
