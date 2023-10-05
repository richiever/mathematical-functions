from sympy import *
import numpy as np

x = Symbol('x')
y = 3*x**5 + 4*x**2 + 7*x**3 + 2*x**4 + x + 7
yprime = y.diff(x)


f,fprime=lambdify(x,y,'numpy'),lambdify(x, yprime, 'numpy')

new_val = 0

count = 0
print("😮\t😮\t😮\t😮\t😮\t😮\t😮\t😮")
print("x_n\t\t\tf(x_n)\t\t\tf'(x_n)")

while (f(new_val) <= -1 * 10**-9 or f(new_val) >= 1 * 10**-9) and count <= 10:
    stored_value_x, stored_value_y,stored_value_dy = round(new_val,5), round(f(new_val),3), round(fprime(new_val),3)
    
    new_val = new_val - (f(new_val) / fprime(new_val))
    print(str(stored_value_x),"\t\t\t",str(stored_value_y),"\t\t\t",str(stored_value_dy))
    count+=1

print("\n\n", "f(", str(new_val), ") = ", str(f(new_val)))