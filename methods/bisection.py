import numpy as np
from math import *

def f(x):
    return x + np.log(x);
    
def bisection(f,a,b,tol,n):
    
    if f(a)*f(b)>=0:
        print("the interval does not change sign");
        
    e_abs = abs(b-a);
    i = 1;
    while i <= n and e_abs > tol:
        c = (a + b)/2;
        print("ite",i,"a =",a,"b =",b,"c =",c);
        if f(c)==0:
            print("solution found in x =", c);
            break;
        if f(a)*f(c)<0:
            b = c;
            c_t = a;
        else:
            a = c;
            c_t = b;
        e_abs = abs(c_t - c);
        if e_abs < tol:
            print("Solution found in x =", c, ",iteration: ", i);
            break;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
            
bisection(f,0.2,1.4,10**-4,50);                              