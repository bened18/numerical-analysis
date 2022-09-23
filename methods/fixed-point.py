from math import *

function = input("enter the function");
x0 = float(input("enter starting value")); 
tol = float(input("enter tolerance"));            #request data from the user
itermax = int(input("enter maximum number of iterations"));

def g(x):
    return eval(function);           #evaluate the function

def punto_fijo(x0, tol, itermax):   
    iter = 1;
    while iter<=itermax:            
       
        x1 = g(x0);                 #evaluate function in last point 
        error = abs((x1-x0)/x1);    
        print("iteration", iter, "point", iter, "function", x1, "error", error); #show table
        
        if error < tol:             #if we reach the desired tolerance stop
            print("solution not found in iteration:", iter, "with x=", x1 );
            return x1;
        
        x0 = x1;                
        iter += 1;               
    
    print("solution not found, iterations used: ", iter);  
    return None;

punto_fijo(x0, tol, itermax);
        