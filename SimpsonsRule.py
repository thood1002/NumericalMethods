#Taylor Hood
#This program uses Simpson's Rule to approximate area
#To use this for any other problem, just swap out the f(x) value and your a,b, and n values
#a = lower bound, b= upper bound 

import math

def f(x):
    return math.exp(-x**2)

def Simpsons(a, b, n):
    # Getting the width of each subinterval or deltaX
    deltaX = (b - a) / n

    # Creating a list of x-values at each subinterval
    x = [a + i * deltaX for i in range(n + 1)]

    # Getting the corresponding y-values using the given function f(x)
    y = [f(xi) for xi in x]

    result = y[0] + y[n]

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * y[i]  # If i is even, weight the value by 2
        else:
            result += 4 * y[i]  # If i is odd, weight the value by 4

    # Multiply the final result by deltaX / 3
    return result * deltaX / 3

# Define intervals and n vals
a = -1
b = 1
n = 80

area = Simpsons(a, b, n)

print("Area is approximately: ", area)
