class Employee:
    def __init__(self):
        print("constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super(). __init__()
        print("constructor of Manager")
    c = 3

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)