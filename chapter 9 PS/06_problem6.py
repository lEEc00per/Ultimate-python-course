with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes")
else:
    print("No")