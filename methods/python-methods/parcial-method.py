from re import A
import numpy as np
from math import *
from tabulate import tabulate


def f(x):
    return np.exp(x-0.5)-0.5*(x**2)-0.5*x-0.625;
def df(x):
    return -x+np.exp(x-0.5)-0.5;
def d2f(x):
  return np.exp(x-0.5)-1;
    
def parcial(f, df,d2f, p_0, tol, n):
    resultados=[[0, p_0, f(p_0),""]]
    e_abs = 1;
    i = 1;
    while i <= n:
        
        if (float(f(p_0))*float(d2f(p_0))-(np.power(df(p_0),2))-(np.power(f(p_0),4))) == 0: #division by zero
            print("solution not found, derivative is zero");
            break;
            
        p_1 = p_0 - (((f(p_0))*(df(p_0))-(np.power(f(p_0),3)))/((f(p_0))*(d2f(p_0))-(np.power(df(p_0),2))-(np.power(f(p_0),4)))); #method formula
        e_abs = abs(p_1 - p_0);
        resultados.append([i,p_1,f(p_1),e_abs])
        if e_abs < tol: #stop criterion
            print("solution found in x = ", p_1, "iterations: ", i);
            break;
        p_0 = p_1;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "Xi", "f(xi)", "error"], tablefmt="github", floatfmt=(".16f",".16f")))


parcial(f,df,d2f,1,10**-7,100);