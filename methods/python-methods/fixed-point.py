from math import *
import numpy as np



def g(x):
    return (np.log(np.sin(x)**2+1)) - 1/2;           #evaluate the function

def punto_fijo(x0, tol, itermax):   
    iter = 1;
    while iter<=itermax:            
        x1 = g(x0);                 #evaluate function in last point 
        error = abs((x1-x0)/x1);    
        print("iteration", iter, "point", iter, "function", x1, "error", error); #show table
        
        if error < tol:             #if we reach the desired tolerance stop
            print("solution found in iteration:", iter, "with x=", x1 );
            break;
        
        x0 = x1;                
        iter += 1;               
    
    if iter > itermax:
        print("solution not found, iterations used: ", iter);  
    

punto_fijo(-0.5, 10**-7, 100);
        