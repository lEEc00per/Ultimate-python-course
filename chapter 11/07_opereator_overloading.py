class Number:
    def __init__(self, n):
        self.n = n

    def __add__(self, obj):
        return self.n + obj.n
    
    def __sub__(self, obj):
        return self.n - obj.n
    
    def __mul__(self, obj):
        return self.n * obj.n
    
    def __truediv__(self, obj):
        return self.n / obj.n
    
    def __floordiv__(self, obj):
        return self.n // obj.n

n = Number(1)
m = Number(2)
print(n + m)
print(n - m)
print(n * m)
print(n / m)
print(n // m)

print("----------------------------------------------------")

class Character:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return str(self.name)
    def __len__(self):
        return len(self.name)
c = Character("junaid")
print(str(c))
print(len(c))