import os

# specify the directory you want to list
directory_path = '/'

# List all files and directories in the specifies path
contents = os.listdir(directory_path)

# Print each file and diretory name 
for item in contents:
    print(item)