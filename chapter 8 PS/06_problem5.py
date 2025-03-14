# Inches to Centimeter converter
def conversion():
    a = float(input("Enter length in inches: "))
    b = a*2.54
    if (b==0):
        return 0
        
    print("1. Round Figure")
    print("2. Perfect Value")
    choice = input("Enter your choice (1 or 2): ")
    if choice == '1':
        print(f"The length of {a} in cm is {round(b)}")
    elif choice == '2':
        print(f"The length of {a} in cm is {b}")
    else:
        print("Invalid choice")
conversion()