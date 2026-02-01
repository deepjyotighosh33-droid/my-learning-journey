class Employee:
    language = "Py" # class attribute
    salary = 120000

    def getInfo(self): # writing self is mandatory
        print(f"The language is {self.language}. The salary is {self.salary}.")

    @staticmethod # static method does not take self as parameter
    def greet():
        print("Good Morning")

DJ = Employee()
DJ.language = "Javascript" #instance attribute

DJ.greet()
DJ.getInfo()
# Employee.getInfo(DJ) # This is equivalent to the above line

# self is just a convention, you can use any other name in place of self but it is not recommended.