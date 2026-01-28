class Employee:
    language = "Py" # class attribute
    salary = 120000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

DJ = Employee("DJ", 130000, "Javascript") 
print(DJ.name, DJ.salary, DJ.language)