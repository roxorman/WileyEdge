# Python program that calculates the factorial of a given number using a for loop:

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result
print(factorial(5))