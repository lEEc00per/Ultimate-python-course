try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    if b == 0:
        raise ZeroDivisionError("Hye our program is not meant to divide any number by 0(zero).")
    else:
        print(f"The division of {a} and {b} is {a/b}")
except ValueError:
    print("Please enter a valid number.")