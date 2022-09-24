import numpy as np
from math import *

def f(x):
    return x**x - 100;

def secant(f, p_0, p_1, tol, n):
    e_abs = abs(p_1 - p_0);
    
    print('iteration:',0,'p = ', p_0);
    print('iteration:',1,'p = ', p_1, 'error = ', e_abs);
    
    i = 2;
    while i <= n:
        if f(p_1) == f(p_0): #division by cero
            print('solution not found (error in the initial values)');
            break;
        
        p_2 = p_0 - (f(p_0)*(p_1 - p_0))/(f(p_1) - f(p_0)); # secant method formula
        e_abs = abs(p_2- p_1);
        print('iteration:',i,'p = ', p_2, 'error = ', e_abs);
        
        if e_abs < tol: #stop criterion
            print('solution found in x = ', p_2, 'iterations: ', i);
            break;
        
        p_0 = p_1;
        p_1 = p_2;
        
        i+=1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
        
secant(f,3,3.2,10**-4,50);