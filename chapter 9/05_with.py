f = open("file.txt")
print(f.read())
f.close()

# The same thing can be written by using with statement

with open("file.txt") as f:
    print(f.read())
# There is no need to explicitly close the files