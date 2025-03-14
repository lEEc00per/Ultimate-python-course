class Employee:
    language = "Python" # This is an class attribute
    salary = 1200000

jerry = Employee()
jerry.language = "html" # This is an instance attribute
print(jerry.salary, jerry.language)