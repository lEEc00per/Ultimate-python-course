# Here self is harry. While when we take inputs from the user the self becomes the name entered by the user
class Employee:
    language = "Python" # This is an class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language} and the salary of the developer is {self.salary}")

    @staticmethod # staticmethod has no lena dena with objects and doesn't need anything of object
    def greet():
        print("Good morning")


harry  = Employee()
harry.language = "JavaScript" # This is an object (instance) attribute
# harry.getInfo()     # 1
harry.greet()
Employee.getInfo(harry)# 2
# "harry.getInfo() and Employee.getInfo(harry)" These are both the same ways to run a define, i.e., (here): def getInfo(self):