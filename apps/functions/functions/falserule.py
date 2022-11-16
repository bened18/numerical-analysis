import numpy as np
from tabulate import tabulate


def f(x):
    return (np.log(np.sin(x)**2+1)) - 1/2


def false_position(a=0, b=1, tol=10**-7, n=100):

    if f(a)*f(b) >= 0:
        return("the interval does not change sign")

    resultados = []

    e_abs = abs(b-a)

    i = 1

    c = a - (f(a)*(b-a))/(f(b)-f(a))

    while i <= n:
        c_1 = c
        resultados.append([i, '%.10f' % a, c_1, b, f(c_1), e_abs])
        if f(c_1) == 0:
            break
        if f(a)*f(c) < 0:
            b = c_1
        else:
            a = c_1
        c = a - (f(a)*(b-a))/(f(b)-f(a))
        if e_abs < tol:
            break
        e_abs = abs(c_1 - c)
        i += 1

    if i > n:
        return("solution not found for tolerance:",
              tol, "spend iterations:", i-1)

    return(tabulate(resultados, headers=[
          "iter", "a", "xm", "b", "f(xm)", "error"], tablefmt="html"))
