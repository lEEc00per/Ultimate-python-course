from functools import reduce
# Map example 

l = [1, 2, 3, 4, 5]

square = lambda x:x*x

sqList = map(square, l)
print(list(sqList))

# Filter example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven = filter(even, l,)
print(list(onlyEven))

# Reduce example
def sum(a, b):
    return a + b

mul = lambda a, b: a * b
print(reduce(sum, l))
print(reduce(mul, l))