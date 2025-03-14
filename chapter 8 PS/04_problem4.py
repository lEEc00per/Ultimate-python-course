def addition(n):
    if (n==1):
        return 1
    elif (n==0):
        return 0
    else:
        return n + addition(n-1)
n = int(input("Enter a number: "))
print(f"The addition of first {n} natural numbers is {addition(n)}")