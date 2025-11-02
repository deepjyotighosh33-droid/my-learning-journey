def pattern(n):
    if(n==0):
        return 1
    print("*" * n)
    pattern(n - 1)

pattern(1)