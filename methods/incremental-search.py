from math import *

function = input("enter function ");
x0 = float(input("enter starting value ")); 
delta = float(input("enter interval size "));             #request data from the user
itermax = int(input("enter maximum number of iterations "));

def f(x):                                       
    return eval(function);                               #evaluate function


def busquedaincremental(x0, delta, itermax):
    
    iteration = 1;
    x1 = x0 + delta;                               
    mp =  f(x0) * f(x1);        #check if there is a change of sign
    
    if mp <0:
        print("the interval entered [", x0,"," ,x1,"] has a root");

    while (iteration<=itermax):      
        
        print("iteration" , iteration, "[",x0,",",x1,"]", "f(x) =", mp);     
        
        if mp<0:
            print("the interval with possible root is [", x0, ",", x1, "]");  
            break;
        
        x0 = x1;                            
        x1 = x0 + delta;  
        mp = f(x0) * f(x1);               
        
        iteration = iteration + 1;
        
    print("Solution not found, iterations consumed");
                       
     
    
    
busquedaincremental(x0,delta,itermax);