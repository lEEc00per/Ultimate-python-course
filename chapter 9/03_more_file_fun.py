def option1():
    f = open("file.txt")
    lines = f.readlines()
    print(lines, type(lines))
    f.close()
    print("---------------------------------------------")
option1()

def option2():
    f = open("file.txt")
    line1 = f.readline()
    print(line1, type(line1))

    line2 = f.readline()
    print(line2, type(line2))

    line3 = f.readline()
    print(line3, type(line3))

    line4 = f.readline()
    print(line4, type(line4))

    line5 = f.readline()
    print(line5 == "")  #The 5th line of file.txt is empty, hence it will show True if the "" are empty and flase if there is something written in ""

    f.close()
    print("--------------------------------------------")
option2()

def option3():
    f = open("file.txt")
    line = f.readline()
    while(line != ""):
        print(line)
        line = f.readline()
option3()