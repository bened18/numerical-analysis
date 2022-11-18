import numpy as np
from tabulate import tabulate
from math import *
from sympy import *


def f(function, x):
    return eval(function)


def df(function, x):
    return eval(f"{diff(function)}")


def newton(function, p_0, tol, n):
    resultados = [[0, p_0, f(function, p_0), ""]]
    e_abs = 1
    i = 1

    solution = ""

    while i <= n:
        if df(function, p_0) == 0:  # division by zero
            solution = "solution not found, derivative is zero"

        p_1 = p_0 - (f(function, p_0))/(df(function, p_0))  # method formula
        e_abs = abs(p_1 - p_0)
        resultados.append([i, p_1, f(function, p_1), e_abs])
        if e_abs < tol:  # stop criterion
            solution = f"solution found in x = {p_1} iterations: {i}"
            break
        p_0 = p_1
        i += 1
    if i > n:
        solution = f"solution not found for tolerance: {tol} spend iterations:{i-1}"

    return solution, tabulate(
            resultados,
            headers=["iter", "Xi", "f(xi)", "error"],
            tablefmt="html",
            floatfmt=(".10f", ".10f")
        )


# print(newton("x-cos(x)", 1, 0.01, 20)[0])
# print(newton("x-cos(x)", 1, 0.01, 20)[1])
