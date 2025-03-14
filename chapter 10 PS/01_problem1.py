class Programmer:
    company = "Microsoft"
    name = input("Enter your name: ")
    language = input("Enter your language: ")
    salary = input("Are you a fresher? (yes/no): ")
    if salary == "yes":
        print("Your salary is 40,000₹")
        salary = 40000
    elif salary == "no":
        print("Your salary is 85,000₹")
        salary = 85000
    else:
        print("Invalid input")
        
p = Programmer()
content = (p.company, p.name, p.language, p.salary)
content = str(content)
with open("info.txt", "w") as f:
    f.write("'company', 'name', 'language', salary\n")
    f.write(content)