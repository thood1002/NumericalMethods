import math

#This program uses the Secant Method to solve x^2 - e^-x + 2x + lnx and stops when it finds a solution accurate within tol 10^-6

def secantMethod(f, P0, P1, tol):
    iteration = 0

    while iteration < 100:
        #Secant Method formula
        nextP = P1 - f(P1) * (P1 - P0) / (f(P1) - f(P0))
        
        # Check if the absolute difference between nextP and P1 is less than the tolerance
        if abs(nextP - P1) < tol:
            return nextP
        
        # Update P0 and P1 for the next iteration
        P0 = P1
        P1 = nextP

        iteration += 1

# Define the equation
def equation(x):
    return x**2 - math.exp(-x) + 2*x + math.log(x)

#Set Initial guesses
P0 = 1.0
P1 = 2.0

#Set Tolerance
tol = 1e-6

# Call the Secant Method function
result = secantMethod(equation, P0, P1, tol)
#Show answer within tolerance 10e^-6 (6 places after the decimal)
print(f"The root is approximately x = {result:.6f}")
