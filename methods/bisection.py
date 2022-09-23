import numpy as np
from math import *

function = input("enter the function ");
a = float(input("enter interval a "));                              
b = float(input("enter interval b "));
tol = float(input("enter tolerance "));
n = int(input("enter maximum number of iterations "));

                        
    
def bisection(function,a,b,tol,n):
    
    def f(x):
        return eval(function);
    
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
            
bisection(function,a,b,tol,n);                          
