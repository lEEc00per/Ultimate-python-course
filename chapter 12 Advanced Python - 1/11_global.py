a = 89 # global  variable
def fun():
    global a
    a = 3 # local  variable
    print(a)

print(a)
fun()