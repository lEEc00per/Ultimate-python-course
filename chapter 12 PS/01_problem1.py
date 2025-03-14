try:
    with(
        open("file1.txt") as f1, 
        open("file2.txt") as f2,
        open("file3.txt") as f3,
        ):
        f1.write("Hello")
        f2.write("World")
        f3.write("Python")
except FileNotFoundError:
    print("The file which you are trying to open does not exist.")
    print("Thank you!")