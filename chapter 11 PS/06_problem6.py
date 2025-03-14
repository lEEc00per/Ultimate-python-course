class string:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        result =  string(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __str__(self):
        return f"{self.x}i, {self.y}j, {self.z}k"

# Test the implementation
v1 = string(1, 2, 3)
v2 = string(4, 5, 6)
v3 = string(7, 8, 9)  # Same dimension vector

print(v1 + v2)
print(v1 * v2)

print(v1 + v3)
print(v1 * v3)