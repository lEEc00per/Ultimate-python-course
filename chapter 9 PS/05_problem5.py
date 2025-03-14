words = ["Donkey", "bad", "honorable", "behaviour"]

with open("donkey.txt", "r") as f:
    content = f.read()
    print(content)
for word in words:
    content = content.replace(word, "#" * len(word))

with open("donkey.txt", "w") as f:
    f.write(content)