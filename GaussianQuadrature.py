#Taylor Hood
#Math 392
#Program Assignment 5

#This program uses Gaussian Quadrature to approximate the integral of e^(-x^2) from 1 to -1. You can use any n value from 2 to 5.

import numpy as np
from scipy.integrate import quad # Import the quad function to help approximate the integral of f(x) over the interval [-1, 1]

    # Define the function f(x) 
def f(x):
    return np.exp(-x**2)

n = int(input("Enter the value of n (2, 3, 4, or 5): "))  # Prompt the user to enter a value for n

    # Check if the entered value of n is valid (2, 3, 4, or 5)
if n in [2, 3, 4, 5]:
    result, _ = quad(f, -1, 1) # Use quad function to approximate the integral of f(x) from -1 to 1 and print the result
    print(f"Approximate integral for n = {n}: {result}")
else:
    print("Invalid input. Please enter 2, 3, 4, or 5 for n.")
    

#Using the quad funtion felt too easy so I remade a different version that just hard codes the nodal values and weights for each option instead just in case

#def f(x):
#    return np.exp(-x**2)
#
#def gaussQuadIntegral(n):
#    if n == 2:
#        nodes = [-0.577350269189626, 0.577350269189626]
#        weights = [1, 1]
#    elif n == 3:
#        nodes = [-0.774596669241483, 0, 0.774596669241483]
#        weights = [0.555555555555556, 0.888888888888889, 0.555555555555556]
#    elif n == 4:
#        nodes = [-0.861136311594053, -0.339981043584856, 0.339981043584856, 0.861136311594053]
#        weights = [0.347854845137454, 0.652145154862546, 0.652145154862546, 0.347854845137454]
#    elif n == 5:
#        nodes = [-0.906179845938664, -0.538469310105683, 0, 0.538469310105683, 0.906179845938664]
#        weights = [0.236926885056189, 0.478628670499366, 0.568888888888889, 0.478628670499366, 0.236926885056189]
#    else:
#        raise ValueError("n must be 2, 3, 4, or 5")
#
#    integral = 0
#    for i in range(n):
#        integral += weights[i] * f(nodes[i])
#
#    return integral
#
#n = int(input("Enter the value of n (2, 3, 4, or 5): "))
#
#if n in [2, 3, 4, 5]:
#    result = gaussQuadIntegral(n)
#    print(f"Approximate integral for n = {n}: {result}")
#else:
#    print("Invalid input. Please enter 2, 3, 4, or 5 for n.")
