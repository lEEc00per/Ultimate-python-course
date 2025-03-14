is_running = True
while is_running:
    try: 
        a = int(input("Enter a number: "))
        b = int(input("Enter a number: "))

        c = a/b
        print(c)
    except NameError:
        print("Please enter a valid number")

    except ValueError:
        print("Please enter a valid number")
        
    except ZeroDivisionError:
        print("Division by zero is not allowed")

    if a == 000:
        is_running = False
    elif b == 000:
        is_running = False
    else:
        is_running = True