import numpy as np
from math import *
from tabulate import tabulate

def f(function, x):
    return eval(function)

def secant(function, p_0, p_1, tol, n):
    e_abs = abs(p_1 - p_0)
    i = 2
    resultados =[[0,p_0,f(function, p_0),""]]
    resultados.append([1,p_1,f(function, p_1),""])
    
    solution = ""
    table_solution = ""
    
    if tol <= 0:
        solution = "Tolerance must be positive"
        return solution, table_solution
    
    while i <= n:
        if f(function, p_1) == f(function, p_0): #division by cero
            return 'solution not found (error in the initial values)'
        
        p_2 = p_0 - (f(function, p_0)*(p_1 - p_0))/(f(function, p_1) - f(function, p_0)) # secant method formula
        e_abs = abs(p_2- p_1)
        #return('iteration:',i,'p = ', p_2, 'error = ', e_abs)
        resultados.append([i,p_2,f(function, p_2),e_abs]) 
        
        if e_abs < tol: #stop criterion
            break
        
        p_0 = p_1
        p_1 = p_2
        
        i+=1
    if i > n:
        solution = f"solution not found for tolerance: {tol} spend iterations: {i-1}"   
    table_solution = tabulate(resultados, headers=["iter", "Xi", "f(xi)", "error"], tablefmt="html",floatfmt=(".10f",".10f"))
    
    if i < n:
        solution = f"Approximation of root found in x = {p_2}"
    
    return (solution, table_solution)
        
#secant("12*pow(x,4)-2.72*pow(x,3)+0.0042*x",12,18,10**-5,100)