from math import *
import numpy as np
from tabulate import tabulate


def g(g, x):
    return eval(g)


def f1(f1, x):
    return eval(f1)


def fixed_point(g, f1, x0, tol, itermax):
    iter = 0
    resultados = [[iter, x0,  g(g, x0), f1(f1, x0), "NA"]]
    while iter <= itermax:
        x1 = g(g, x0)  # evaluate function in last point
        error = abs(f1(f1, x0))
        x0 = x1
        iter += 1
        resultados.append([iter, x0, g(g, x0), f1(f1, x0), error])
        if error < tol:  # if we reach the desired tolerance stop
            break
    if iter > itermax:
        return f"solution not found, iterations used: {iter}"

    return (tabulate(resultados, headers=["iteration", "Xi", "g(xi)", "f(x)", "error"], tablefmt="html", floatfmt=(".10f", ".10f", ".10f")))

# punto_fijo(-0.5, 10**-7, 100)
