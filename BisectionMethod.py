#Taylor Hood 
#Program Assignment 1 - Bisection
#9/5/2023
#CMPS 392

#Defining function 0 = 3(x+1)(x-1/2)(x-1)
def f(x):
    return 3 * (x + 1) * (x - 1/2) * (x - 1)
  
#Beginning points and n value
a = -2
b = 1.5
n = 26

#Bisection Method
for i in range(0,n): 
    p = 1/2 * (a + b) #finding the midpoint
    
    if(f(p) == 0):
        print(p)
        break #if we have answer, stop and print it
    elif(f(a) * f(p) < 0):
        b = p 
    else:
        a = p

print("Solution is", p)