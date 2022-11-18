from math import *
import numpy as np
from tabulate import tabulate
from sympy.parsing.sympy_parser import parse_expr
from sympy import diff


def fun(function, x):
    eval_f = eval(f"{function}")
    return eval_f, function


def dfun(function, x):
    df = diff(fun(function, x)[1])
    eval_df = eval(f"{df}")
    return eval_df, df


def d2fun(function, x):
    d2f = diff(dfun(function, x)[1])
    eval_d2f = eval(f"{d2f}")
    return eval_d2f, d2f


def multipleroot(function, x0, tol, n):
    xant = x0
    fant = fun(function, xant)[0]
    e_abs = 1000
    iteration = 0
    results = [[iteration, xant, fun(function, xant)[0], ""]]
    dfunction = dfun(function, xant)[1]
    d2function = d2fun(function, xant)[1]
    
    solution = ""
    solution_table = ""

    while iteration <= n:
        xact = xant - fant * dfun(dfunction, xant)[0] / ((dfun(dfunction, xant)[0]) ** 2 - fant * d2fun(d2function, xant)[0])
        fact = fun(function, xact)[0]
        e_abs = abs(xact-xant)
        iteration += 1
        xant = xact
        fant = fact
        results.append([iteration, xant, fun(function, xant)[0], e_abs])

        if e_abs < tol:
            solution = f"Solution found in X = {xact}, iterations:  {iteration-1}  error = {e_abs}"
            solution_table = tabulate(results, headers=["iter", "Xi", "f(x)", "error"], tablefmt="html")
            break

    if iteration > n:
        solution = f"Solution not found for tolerance = {tol}"    
    
    return solution, solution_table

# print(multipleroot("x**2-x-1",1,0.000007,100))
