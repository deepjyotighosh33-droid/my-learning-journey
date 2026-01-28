# Demonstrating the difference between class attributes and instance attributes

class Employee:
    language = "Py" # class attribute
    salary = 120000

DJ = Employee()
DJ.language = "Javascript" #instance attribute
print(DJ.language, DJ.salary)
