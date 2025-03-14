class Employee:
    a = "class attribute"
    @classmethod
    def show1(cls):
        print(f"The class attribute of a is {cls.a}")
    
    def show2(self):
        print(f"The instance attribute of a is {self.a}")

e = Employee()
e.a = "Instance attribute"

e.show1()
e.show2()