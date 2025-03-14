class Employee:
    language = "Python" # This is an class attribute
    salary = 1200000

    def __init__(self, name, salary, language): # dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an obejct")

    def getInfo(self):
        print(f"The language is {self.language} and the salary of the developer is {self.salary}")

    @staticmethod # staticmethod has no lena dena with objects and doesn't need anything of object
    def greet():
        print("Good morning")


harry  = Employee("Harry", 1300000, "JvaScript")
print(harry.name, harry.salary, harry.language)