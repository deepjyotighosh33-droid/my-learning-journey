'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 1 x 2
factorial(3) = 1 x 2 x 3

factotial(n) = n x n-1 x......3 x 2 x 1

factorial(n) = n * factorial(n -1)
'''

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

n = int(input("Enter no: "))
print(f"The Factorial of no is: {factorial(n)}")
