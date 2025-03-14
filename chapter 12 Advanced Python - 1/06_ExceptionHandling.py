def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
    except ValueError:
        print("Invalid Input")
main()

def men():
    try:
        a = int(input("Enter a number: "))
        print(a)
    except Exception as e:
        print(e)
        print("Thank you")
men()