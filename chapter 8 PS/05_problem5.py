def pattern(n):
    if n==0:
        return 
    print("*" * n)
    pattern(n-1)

for i in range(3):
    n = int(input("Enter a number: "))
    pattern(n)
    print("_"* 154)