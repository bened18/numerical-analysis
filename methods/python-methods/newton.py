from re import A
import numpy as np
from math import *
from tabulate import tabulate


def f(x):
    return (np.log(np.sin(x)**2+1)) - 1/2;
def df(x):
    return (2 * (np.sin(x)**2 + 1)**-1) * (np.sin(x) * np.cos(x));
    
def newton(f, df, p_0, tol, n):
    print("iteration: ", 0, "p = ", p_0);
    resultados=[[0, p_0, f(p_0),""]]
    e_abs = 1;
    i = 1;
    while i <= n:
        if df(p_0) == 0: #division by zero
            print("solution not found, derivative is zero");
            break;
            
        p_1 = p_0 - (f(p_0))/(df(p_0)); #method formula
        e_abs = abs(p_1 - p_0);
        resultados.append([i,p_1,f(p_1),e_abs])
        if e_abs < tol: #stop criterion
            print("solution found in x = ", p_1, "iterations: ", i);
            break;
        p_0 = p_1;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "Xi", "f(xi)", "error"], tablefmt="github", floatfmt=(".10f",".10f")))


newton(f,df,0.5,10**-7,100);