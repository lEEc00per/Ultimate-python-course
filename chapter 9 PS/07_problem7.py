with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in line):
        print(f"Python is present on the line: {lineno}")
        break
    lineno += 1
else:
    print("No Python is not present in log.txt")