class Calculator():

    def square(self):
        number = float(input("Enter a number: "))
        print (f"the answer is  {number} is {number * number}")

    def cube(self):
        number = float(input("Enter a number: "))
        print (f"the answer is  {number} is {number * number * number}")

    def square_root(self):
        number = float(input("Enter a number: "))
        if number < 0:
            print("Cannot calculate square root of a negative number")
        else:
            print (f"the answer is  {number} is {number ** 0.5}")

c = Calculator()

is_running = True
while is_running:
    print("1. SQUARE")
    print("2. CUBE")
    print("3. SQUARE ROOT")
    print("4. EXIT")
    choice = input("Enter your choice: ")
    if choice == '1':
        c.square()
    elif choice == '2':
        c.cube()
    elif choice == '3':
        c.square_root()
    elif choice == '4':
        is_running = False
    else:
        print("Invalid choice")
print("\t Thank you, visit again...")