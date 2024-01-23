#Taylor Hood
#MATH 392
#Program Assignment 3

#This Program uses Newton's Method with Synthetic Division to find the first positive root to the problem below with accuracy within 10^-5. 
#Polynomial used atm:(f(x) = x^6 + 5x^3 - 85x - 136).
#The code should be able to run for a polynomial of any degree.
#Remember the format for putting in coefficients when trying to test other problems(on line 41) 
#p.s. do not forget to change initial guess when trying different problems

import sympy as sp

#Finding the derivative of a polynomial
def derivative(coefficients):
    n = len(coefficients)
    return [coeff * (n - i - 1) for i, coeff in enumerate(coefficients[:-1])]

#Newtons method to find the root of the polynomial
def newtonsMethod(coefficients, x0, tolerance=1e-5, maxIterations=100):
    for i in range(maxIterations):
        fx0 = syntheticDivision(coefficients, x0)
        fprimex0 = syntheticDivision(derivative(coefficients), x0)
        x1 = x0 - fx0 / fprimex0

        if abs(x1 - x0) < tolerance:
            return x1
        x0 = x1
    return 0

#Synthetic Division funtion
def syntheticDivision(coefficients, x):
    result = 0
    for coeff in coefficients:
        result = result * x + coeff
    return result

def findRoot(coefficients, guess, tolerance=1e-5):

    # Find the root
    root = newtonsMethod(coefficients, guess, tolerance=tolerance)
    return root

# Coefficients of the polynomial f(x) = x^6 + 5x^3 - 85x - 136 (0's represent missing coeffs)
coefficients = [1, 0, 0, 5, 0, -85, -136]

# Initial guess for the root
x0 = 2.0

root = findRoot(coefficients, x0)
#Displaying the approximation
print(f"The root is approximately: {root:.5f}")

