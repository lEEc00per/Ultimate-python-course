a = (int(input("Enter your age: ")))

# "If", "Elif", "Else" Ladder

if(a>18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("It ia an invalid negative age")

elif(a==0):
    print("You have entered a 0, which is not a valid age")

else:
    print("You are below the age of consent")

print("End of the program")