import numpy as np
from tabulate import tabulate


def f(function, x):
    return eval(function)


def df(dfunction, x):
    return eval(dfunction)


def newton(function, dfunction, p_0, tol, n):
    resultados = [[0, p_0, f(function, p_0), ""]]
    e_abs = 1
    i = 1

    solution = ""
    solution_not_found = ""
    solution_div_by_zero = ""

    while i <= n:
        if df(dfunction, p_0) == 0:  # division by zero
            solution_div_by_zero = "solution not found, derivative is zero"

        p_1 = p_0 - (f(function, p_0))/(df(dfunction, p_0))  # method formula
        e_abs = abs(p_1 - p_0)
        resultados.append([i, p_1, f(function, p_1), e_abs])
        if e_abs < tol:  # stop criterion
            solution = f"solution found in x = {p_1} iterations: {i}"
        p_0 = p_1
        i += 1
    if i > n:
        solution_not_found = f"solution not found for tolerance: {tol} spend iterations:{i-1}"

    if solution != "":
        return (solution, tabulate(
            resultados,
            headers=["iter", "Xi", "f(xi)", "error"],
            tablefmt="html",
            floatfmt=(".10f", ".10f")
        ))

    if solution_div_by_zero != "":
        return solution_div_by_zero

    if solution_not_found != "":
        return solution_not_found


# print(newton(0.5, 10**-7, 100)[0])
# print(newton(0.5, 10**-7, 100)[1])
