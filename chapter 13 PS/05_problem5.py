from functools import reduce
l = [1,51,51,88,8,6,654,2031,54,87,898,117,567]

def main(a, b):
    if (a > b):
        return a
    return b
print(reduce(main, l))