# multiplies a number n by all integers from 1 to n and prints the results

def multiply(n):
    for i in range(1, n+1):
        print(f"{n} x {i} = {n*i}")

multiply(5)