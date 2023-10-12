

import math
import time
def f(x):

    return x*x*x+12*x*x+48*x+66
def bisection(a,b, func):
    
        
    
        c = a
    
        while (b-a) >= 0.01:
            
            c = (a+b)/2
            print(c)

            if func(c) == 0.0:
    
                break
    
            if func(c)*func(a)< 0:
                
                b = c
    
            else:
    
                a = c
    
        print(f"The value of root is : {c:.4f}")



st = time.time()

bisection(-6, 0, f)

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
