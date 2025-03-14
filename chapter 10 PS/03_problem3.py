class Demo:
    a = 4

o = Demo()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # The instance attribute is set
print(o.a) # Prints the instance attribuete because instance attribute is set
print(Demo.a) # prints the class attribute