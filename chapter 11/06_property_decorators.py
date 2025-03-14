# There is no any instance attribute in this program

class Employee:
    user = input("Enter your name: ")
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.name = e.user
print(e.fname, e.lname)