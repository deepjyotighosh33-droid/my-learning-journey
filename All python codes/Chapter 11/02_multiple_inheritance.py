class Employee:               # Base Class
    company = "ITC"
    name = "Default Name"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")

class coder:                  # Base Class
    language = "Python"
    def printLanguages(self):
        print(f"Out of all the languages here is your language: {self.language}")

class Programmer(Employee, coder):    # Child Class
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()
