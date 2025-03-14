def main(name, marks, phone):
    name = input("Enter your name: ")
    marks = input("Enter your marks: ")
    phone = input("Enter your phone number: ")
    print(f"The name of the student is {name}, his marks are {marks} and the phone number is {phone}")
main("name", "marks", "phone")

# another method
name = input("Enter your name: ")
marks = input("Enter your marks: ")
phone = input("Enter your phone number: ")
a = "The name of the student is {}, his marks are {} and the phone number is {}".format(name, marks, phone)
print(a)