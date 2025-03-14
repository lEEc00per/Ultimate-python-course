'''
1 = snake 
-1 = water
0 = gun
'''
def main():

    import random
    computer = random.choice([1, -1, 0])
    youstr = input("Enter your choice: ")
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    you = youDict[youstr]
    # By now we have twon numbers (variables), you and the computer

    print(f"You chose {reverseDict[you]}\nand computer chose {reverseDict[computer]}")
    if (computer == you):                                          #
        print("It is a draw")                                      #
    else:                                                          #
        if((computer - you) == -1 or (computer - you) == 2):       #  
            print("You Lose!")                                     # Shortened part
        elif ((computer - you) == 1 or (computer - you) == -2):    #
            print("You won!")                                      #
        else:                                                      #
            print("Something went wrong!")                         #
main();main();main()
    # if (computer == -1 and you == 1):
    #     print("You won!")
    # elif (computer == -1 and you == 0):
    #     print("You lost")
    # elif (computer == 1 and you == -1):
    #     print("You lost")
    # elif (computer == 1 and you == 0):
    #     print("You won!")
    # elif (computer == 0 and you == 1):
    #     print("You lost")
    # elif (computer == 0 and you == -1):
    #     print("You won!")
    # else:
    #     print("try again")
#main();main();main()