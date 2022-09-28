import numpy as np
from math import *
from tabulate import tabulate

def f(x):
    return (np.log(np.sin(x)**2+1)) - 1/2;
    
def bisection(f,a,b,tol,n):
    resultados=[]
    if f(a)*f(b)>=0:
        print("the interval does not change sign");
        
    e_abs = abs(b-a);
    i = 1;
    while i <= n and e_abs > tol:
        c = (a + b)/2;
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
        if(i!=1):
            resultados.append([i,a,c,b,f(c),e_abs])
        else:
            resultados.append([i,a,c,b,f(c),""])


        if e_abs < tol:
            print("Solution found in x =", c, ",iteration: ", i);
            break;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="github", floatfmt=(".0f",".10f",".10f",".10f")))
            
bisection(f,0,1,10**-7,100);                              