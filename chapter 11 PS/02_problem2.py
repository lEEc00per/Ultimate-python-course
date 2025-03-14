class Animals:
    pass
class pets(Animals):
    pass
class Dog(pets):
    @staticmethod
    def bark():
        print("bow! bow!")

d = Dog()
d.bark()