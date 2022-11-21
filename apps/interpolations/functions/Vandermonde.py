import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate

import json


def convert_string_to_list(string):
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json


#xi = "-1,0,3,4"
#fi = "15.5,3,8,1"


def vandermonde(xi_str, yi_str):
    muestras = 101
    xi = np.array(convert_string_to_list(xi_str))
    B = np.array(convert_string_to_list(yi_str))
    n = len(xi)
    D = np.zeros(shape=(n, n), dtype=float)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            potencia = (n-1)-j
            D[i, j] = xi[i]**potencia

    coeficiente = np.linalg.solve(D, B)

    x = sym.Symbol('x')
    polinomio = 0
    for i in range(0, n, 1):
        potencia = (n-1)-i
        termino = coeficiente[i]*(x**potencia)
        polinomio = polinomio + termino

    resultado = ""
    #return('Vandermonde: ')
    #return((tabulate(D, tablefmt="html")))
    resultado = resultado + (tabulate(D, tablefmt="html"))
    #return('Polynomial coefficients: ')
    resultado = resultado + '\nPolynomial coefficients: \n'
    resultado = resultado + str(coeficiente)
    # return(coeficiente)
    #return('Interpolation polynomial: ')
    resultado_polynomial = resultado + '\nInterpolation polynomial: \n'
    resultado = resultado + str(polinomio)
    # return(polinomio)
    #return('\n ')
    # sym.preturn(polinomio)
    return resultado

# GRAFICACION DEL EJERCICIO
# --------------------------------------------
# # px = sym.lambdify(x,polinomio)
# a = np.min(xi)
# b = np.max(xi)
# xin = np.linspace(a,b,muestras)
# yin = px(xin)
# plt.plot(xi,fi,'o', label='[xi,fi]')
# plt.plot(xin,yin, label='p(x)')
# plt.xlabel('xi')
# plt.ylabel('fi')
# plt.legend()
# plt.title(polinomio)
# plt.show()
# --------------------------------------------


#print(vandermonde(xi, fi))
