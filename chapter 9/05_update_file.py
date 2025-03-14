#Update using r+:
write = "I have updated the file using r+"

file = open("file.txt", "r+")

content = file.read()

file.seek(0)

file.write(write)

file.write(content)

file.close()

#Update using w+:
file = open("file.txt", "w+")

file.seek(0)

file.write("New Content\n")

print(file.read())

file.close()