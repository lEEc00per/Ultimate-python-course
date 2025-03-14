import os

current_file = "rename.txt"
new_file = "renamed_by_python.txt"

os.rename(current_file, new_file)
print("done")

with open("renamed_by_python.txt", "w") as f:
    f.write("This file is renamed.")