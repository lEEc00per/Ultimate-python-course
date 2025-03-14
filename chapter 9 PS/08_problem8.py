with open("this.txt") as f:
    content = f.read()
    print(content)

with open("thiscopy.txt", "w") as a:
    edit = a.write(content)

print("\n \t The code is successful!")