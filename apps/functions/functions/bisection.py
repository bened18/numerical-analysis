from math import *
from sympy import *
import numpy as np
from tabulate import tabulate

def f(function, x):
    return eval(function)
    
def bisection(function,a,b,tol,n):
    resultados=[]
    solution = ""
    
    if f(function, a)*f(function, b)>=0:
        return("the interval does not change sign")
        
    e_abs = abs(b-a)
    i = 1
    while i <= n and e_abs > tol:
        c = (a + b)/2
        if f(function, c)==0:
            solution = f"solution found in x = {c}"
            break
        if f(function, a)*f(function, c)<0:
            b = c
            c_t = a
        else:
            a = c
            c_t = b
        e_abs = abs(c_t - c)
        if(i!=1):
            resultados.append([i,a,c,b,f(function, c),e_abs])
        else:
            resultados.append([i,a,c,b,f(function, c),""])


        if e_abs < tol:
            solution = f"Solution found in x = {c} | iteration: {i}"
            break
        i += 1
    if i > n:
        solution = f"Solution not found for tolerance:{tol} spend iterations: {i-1}"
    return(solution, tabulate(resultados, headers=["iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="html", floatfmt=(".0f",".10f",".10f",".10f")))
            
#print(bisection("log(pow(sin(x),2)+1)-(1/2)",0,1,10**-7,100))