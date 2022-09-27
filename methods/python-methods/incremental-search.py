from math import *
import numpy as np

def f(x):                                       
    return (np.log(np.sin(x)**2+1)) - 1/2;                               #evaluate function

def incrementalsearch(x0, delta, itermax):
    
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
    if iteration > itermax:
        print("Solution not found, iterations consumed");
    
incrementalsearch(-3,0.5,100);