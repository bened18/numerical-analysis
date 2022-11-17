import numpy as np
from tabulate import tabulate


def f(function, x):
    return eval(function)


def false_position(function, a, b, tol, n):

    if f(function, a)*f(function, b) >= 0:
        return("the interval does not change sign")

    resultados = []

    e_abs = abs(b-a)

    i = 1

    c = a - (f(function, a)*(b-a))/(f(function, b)-f(function, a))

    while i <= n:
        c_1 = c
        resultados.append([i, '%.10f' % a, c_1, b, f(function, c_1), e_abs])
        if f(function, c_1) == 0:
            break
        if f(function, a)*f(function, c) < 0:
            b = c_1
        else:
            a = c_1
        c = a - (f(function, a)*(b-a))/(f(function, b)-f(a))
        if e_abs < tol:
            break
        e_abs = abs(c_1 - c)
        i += 1

    if i > n:
        return("solution not found for tolerance:", tol, "spend iterations:", i-1)

    return(tabulate(resultados, headers=["iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="html"))
