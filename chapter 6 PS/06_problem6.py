a = (float(input("Enter your marks: ")))

if(a<100 and a>=90):
    grade = "Ex"

elif(a<90 and a>=80):
    grade = "A"

elif(a<80 and a>=70):
    grade = "B"

elif(a<70 and a>=60):
    grade = "C"

elif(a<60 and a>=50):
    grade = "D"

elif(a<50):
    grade = "F"

print("Your grade is: ", grade)