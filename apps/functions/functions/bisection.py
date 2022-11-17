import numpy as np
from math import *
from tabulate import tabulate

def f(function, x):
    return eval(function)
    
def bisection(function,a,b,tol,n):
    resultados=[]
    if f(function, a)*f(function, b)>=0:
        return("the interval does not change sign");
        
    e_abs = abs(b-a);
    i = 1;
    while i <= n and e_abs > tol:
        c = (a + b)/2;
        if f(function, c)==0:
            return("solution found in x =", c);
            break;
        if f(function, a)*f(function, c)<0:
            b = c;
            c_t = a;
        else:
            a = c;
            c_t = b;
        e_abs = abs(c_t - c);
        if(i!=1):
            resultados.append([i,a,c,b,f(function, c),e_abs])
        else:
            resultados.append([i,a,c,b,f(function, c),""])


        if e_abs < tol:
            return("Solution found in x =", c, ",iteration: ", i);
            break;
        i += 1;
    if i > n:
        return("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    return(tabulate(resultados, headers=["iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="html", floatfmt=(".0f",".10f",".10f",".10f")))
            
#bisection(f,0,1,10**-7,100);