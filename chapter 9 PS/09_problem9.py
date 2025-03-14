with open("file1.txt") as f:
    content1 = f.read()
    print("FILE 1")
    print(content1)

with open("file2.txt") as f:
    content2 = f.read()
    print("\nFILE2")
    print(content2)

if (content1 == content2):
    print("\n Yes, these files are identical")
else:
    print("\n No, these files are not identical")