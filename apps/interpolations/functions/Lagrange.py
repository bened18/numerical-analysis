import numpy as np
import sympy as sym
import json
from math import *
import matplotlib.pyplot as plt


def convert_string_to_list(string):
    """
        Receive a comma-separated string and convert it to its type
        exm:
            convert_string_to_list("1,2.3,4,5.6")
        result:
            [1,2.3,4,5.6]
            int,float,int,float
    """
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


def lagrange(xi_str, fi_str):
    xi = convert_string_to_list(xi_str)
    fi = convert_string_to_list(fi_str)

    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype=float)
    for i in range(0, n, 1):

        numerador = 1
        denominador = 1
        for j in range(0, n, 1):
            if (j != i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    polisimple = sym.expand(polinomio)

    px = sym.lambdify(x, polisimple)

    muestras = 101
    a = min(xi, default=0)
    b = max(xi, default=0)
    pxi = np.linspace(a, b, muestras)
    pfi = px(pxi)

    return {
        "fi": fi,
        "dividers": divisorL,
        "lpe": polinomio,
        "lp": polisimple,
        "xi": xi,
        "pxi": pxi,
        "pfi": pfi
    }

    # print('    fi values: ',fi)
    # print('dividers L(i): ',divisorL)
    # print()
    # print('Lagrange polynomial, expressions')
    # print(polinomio)
    # print()
    # print('Lagrange polynomial ')
    # print(polisimple)

    # plt.plot(xi,fi,'o', label = 'Point')
    # plt.plot(pxi, pfi, label = 'Polynomial')
    # plt.legend()
    # plt.xlabel('xi')
    # plt.ylabel('fi')
    # plt.title('Lagrange interpolation')
    # plt.show()

# print(lagrange("-1,0,3,4", "15.5,3,8,1"))
