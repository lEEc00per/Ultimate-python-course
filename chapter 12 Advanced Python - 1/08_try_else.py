try:
    a = int(input("Enter a number: "))
    print(a)
except ValueError:
    print("This is a value error.")
else: # This is only if the try was successful.
    print("I am inside else block.")
