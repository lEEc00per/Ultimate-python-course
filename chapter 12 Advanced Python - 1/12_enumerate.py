l = [1, 153, 948, 67, 9887]

# index = 1
# for item in l:
#     print(f"The  item number at index is {index} is {item}")
#     index += 1

# This can be simplified using the enumerate function
for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")