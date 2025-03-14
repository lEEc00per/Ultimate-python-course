word = "Donkey"

with open("donkey.txt", "r") as f:
    content = f.read()
    print(content)

newcontent = content.replace(word, "#####")

with open("donkey.txt", "w") as f:
    f.write(newcontent)