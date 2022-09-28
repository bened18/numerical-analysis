import numpy as np
from math import *
from tabulate import tabulate

def f(x):
        return (np.log(np.sin(x)**2+1)) - 1/2;              
    
def false_position(f,a,b,tol,n):
    if f(a)*f(b)>=0:
        print("the interval does not change sign");
    resultados=[]
    e_abs = abs(b-a);
    i = 1;
    c = a - (f(a)*(b-a))/(f(b)-f(a));
    while i <= n:
        c_1 = c;
        resultados.append([i,'%.10f'%a,c_1,b,f(c_1), e_abs ])
        if f(c_1)==0:
            break;
        if f(a)*f(c)<0:
            b = c_1;
        else:
            a = c_1;
        c = a - (f(a)*(b-a))/(f(b)-f(a));
        if e_abs < tol:
            break;
        e_abs = abs(c_1 - c);
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="github", floatfmt=(".0f",".10f",".10f",".10f")))

false_position(f,0,1,10**-7,100);   

