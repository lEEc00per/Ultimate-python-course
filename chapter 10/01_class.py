class Employee:
    name = input("Enter your name: ") # This is an object(instance) attribute
    language = "Py" # This is a class attribute
    salary = 12000000

Name = Employee()
print(Name.name, Name.language, Name.salary)

# Here name is object(instance) attribute and salary and language are class attributes as they directly belong to the class 