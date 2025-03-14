# New merge feature
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)

# Using the new with function
with(
    open("file1.txt", "w") as f1,
    open("file2.txt", "w") as f2,
):
    f1.write("This is a very good Sunday!")
    f2.write("This is a very good Sunday!")