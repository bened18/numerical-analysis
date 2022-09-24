from re import A
import numpy as np
from math import *

def f(x):
    return x**x - 100;
def df(x):
    return x**x * (np.log(x) + 1);
    
def newton(f, df, p_0, tol, n):
    print("iteration: ", 0, "p = ", p_0);
    e_abs = 1;
    i = 1;
    while i <= n:
        if df(p_0) == 0: #division by zero
            print("solution not found, derivative is zero");
            break;
            
        p_1 = p_0 - (f(p_0))/(df(p_0)); #method formula
        e_abs = abs(p_1 - p_0);
        print("iteration: ", i, "p = ", p_1, "error = ", e_abs);
        
        if e_abs < tol: #stop criterion
            print("solution found in x = ", p_1, "iterations: ", i);
            break;
        p_0 = p_1;
        i += 1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);

newton(f,df,1,10**-10,500);