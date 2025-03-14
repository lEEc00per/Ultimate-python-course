marks1 = (float(input("Enter marks 1: ")))
marks2 = (float(input("Enter marks 2: ")))
marks3 = (float(input("Enter marks 3: ")))
marks4 = (float(input("Enter marks 4: ")))
marks5 = (float(input("Enter marks 5: ")))
marks6 = (float(input("Enter marks 6: ")))

# Check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3 + marks4 + marks5 + marks6))/240

if(total_percentage>=40 and marks1>=14 and marks2>=14 and marks3>=14 and marks4>=14 and marks5>=14 and marks6>=14):
    print("You are passed: ", total_percentage)

else:
    print("You are failed, better luck next year: ", total_percentage)