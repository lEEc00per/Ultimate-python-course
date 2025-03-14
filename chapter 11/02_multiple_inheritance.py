class Employee:
    company = "ITC"
    name = "Default name"
    salary = 40000
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder:
    language  = "Python"
    def printLanguages(self):
        print(f"Out of all languages here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showLanguage()