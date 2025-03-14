def main():
    try:
        a = int(input("Enter a number: "))
        print(a)
    except ValueError:
        print("This is a value error.")
    finally:
        print("I am inside finally block.")
main()