import numpy as np
from math import *
from tabulate import tabulate

def f(x):
    return (np.log(np.sin(x)**2+1)) - 1/2;

def secant(f, p_0, p_1, tol, n):
    e_abs = abs(p_1 - p_0);
    
    
    print('iteration:',0,'p = ', p_0);
    print('iteration:',1,'p = ', p_1, 'error = ', e_abs);
    
    i = 2;
    p_2 = 0;
    resultados =[[i,p_2,f(p_2),""]]
    while i <= n:
        if f(p_1) == f(p_0): #division by cero
            print('solution not found (error in the initial values)');
            break;
        
        p_2 = p_0 - (f(p_0)*(p_1 - p_0))/(f(p_1) - f(p_0)); # secant method formula
        e_abs = abs(p_2- p_1);
        #print('iteration:',i,'p = ', p_2, 'error = ', e_abs);
        resultados.append([i,p_2,f(p_2),e_abs]) 
        
        if e_abs < tol: #stop criterion
            print('solution found in x = ', p_2, 'iterations: ', i);
            break;
        
        p_0 = p_1;
        p_1 = p_2;
        
        i+=1;
    if i > n:
        print("solution not found for tolerance:" , tol,"spend iterations:", i-1);
    print(tabulate(resultados, headers=["iter", "Xi", "f(xi)", "error"], tablefmt="github"))
secant(f,0.5,1,10**-7,100);