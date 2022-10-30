import numpy as np
from math import *
from tabulate import tabulate

def f(x):
    return (12*x**4-2.72*x**3+0.2153*x**2-0.0042*x);

def secant(f, p_0, p_1, tol, n):
    e_abs = abs(p_1 - p_0);
    i = 2;
    resultados =[[0,p_0,f(p_0),""]]
    resultados.append([1,p_1,f(p_1),""])
    while i <= n:
        if f(p_1) == f(p_0): #division by cero
            print('solution not found (error in the initial values)');
            break;
        
        p_2 = p_0 - (f(p_0)*(p_1 - p_0))/(f(p_1) - f(p_0)); # secant method formula
        e_abs = abs(p_2- p_1);
        #print('iteration:',i,'p = ', p_2, 'error = ', e_abs);
        resultados.append([i,p_2,f(p_2),e_abs]) 
        
        if e_abs < tol: #stop criterion
            break;
        
        p_0 = p_1;
        p_1 = p_2;
        
        i+=1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "Xi", "f(xi)", "error"], tablefmt="github",floatfmt=(".10f",".10f")))
    if i < n:
        print('Approximation of root found in x = ', p_2);

secant(f,12,18,10**-5,100);