import numpy as np
from math import *

def f(x):
        return x**x - 100;              
    
def false_position(f,a,b,tol,n):
    
    if f(a)*f(b)>=0:
        print("the interval does not change sign");
        
    e_abs = abs(b-a);
    i = 1;
    c = a - (f(a)*(b-a))/(f(b)-f(a));
    while i <= n and e_abs > tol:
        c_1 = c;
        print("iteration", i, "interval: [",a,",",b,"]","mid point c =", c_1);
        
        if f(c_1)==0:
            print("solution found in x =", c_1);
            break;
        if f(a)*f(c)<0:
            b = c_1;
        else:
            a = c_1;
            
        c = a - (f(a)*(b-a))/(f(b)-f(a));
        
        e_abs = abs(c_1 - c);
        
        if e_abs < tol:
            print("Solution found in x =", c,",", "iteration: ", i);
            break;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
            
false_position(f,3,4,10**-10,50);   