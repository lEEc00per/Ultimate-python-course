def gt(a, b, c):
    if(a>b and a>c):
        return (f"The greatest number is {a}")
    elif(b>a and b>c):
        return (f"The greatest number is {b}")
    elif(c>a and c>b):
        return (f"The greatest number is {c}")

a = int(input("Enter your number: "))
b = int(input("Enter your number: "))
c = int(input("Enter your number: "))
print(gt(a, b, c))