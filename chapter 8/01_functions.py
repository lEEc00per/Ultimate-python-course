# a = (("Enter a number: "))
# b = (("Enter a number: "))
# c = (("Enter a number: "))

# average  = (a+b+c)/3
# print(average)


#Function defination 
def avg():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))

    average  = (a+b+c)/3
    print(average)
    return "Done"

a = avg()# Function call
print(a)
b = avg()
print(b)
c = avg()
print(c)
d = avg()
print(d)
e = avg()
print(e)