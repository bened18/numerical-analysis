# Trazador cúbico natural
import json
import numpy as np
import sympy as sym
from math import *


def convert_string_to_list(string):
    """
        Receive a comma-separated string and convert it to its type
        exm:
            convert_string_to_list("1,2.3,4,5.6")
        result:
            [1,2.3,4,5.6]
            int,float,int,float
    """
    res = f"[{string}]"
    return json.loads(res)


def traza3natural(xi_str, yi_str):
    # parse str to float
    xi = convert_string_to_list(xi_str)
    yi = convert_string_to_list(yi_str)
    
    trazadores_list = []
    n = len(xi)

    # Valores h
    h = np.zeros(n-1, dtype=float)
    for j in range(0, n-1, 1):
        h[j] = xi[j+1] - xi[j]

    # Sistema de ecuaciones
    A = np.zeros(shape=(n-2, n-2), dtype=float)
    B = np.zeros(n-2, dtype=float)
    S = np.zeros(n, dtype=float)
    A[0, 0] = 2*(h[0]+h[1])
    A[0, 1] = h[1]
    B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])
    for i in range(1, n-3, 1):
        A[i, i-1] = h[i]
        A[i, i] = 2*(h[i]+h[i+1])
        A[i, i+1] = h[i+1]
        B[i] = 6*((yi[i+2]-yi[i+1])/h[i+1] - (yi[i+1]-yi[i])/h[i])
    A[n-3, n-4] = h[n-3]
    A[n-3, n-3] = 2*(h[n-3]+h[n-2])
    B[n-3] = 6*((yi[n-1]-yi[n-2])/h[n-2] - (yi[n-2]-yi[n-3])/h[n-3])

    # Resolver sistema de ecuaciones
    r = np.linalg.solve(A, B)
    # S
    for j in range(1, n-1, 1):
        S[j] = r[j-1]
    S[0] = 0
    S[n-1] = 0

    # Coeficientes
    a = np.zeros(n-1, dtype=float)
    b = np.zeros(n-1, dtype=float)
    c = np.zeros(n-1, dtype=float)
    d = np.zeros(n-1, dtype=float)
    for j in range(0, n-1, 1):
        a[j] = (S[j+1]-S[j])/(6*h[j])
        b[j] = S[j]/2
        c[j] = (yi[j+1]-yi[j])/h[j] - (2*h[j]*S[j]+h[j]*S[j+1])/6
        d[j] = yi[j]

    # Polinomio trazador
    x = sym.Symbol('x')
    polinomio = []
    for j in range(0, n-1, 1):
        ptramo = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2 + c[j]*(x-xi[j]) + d[j]
        ptramo = ptramo.expand()
        polinomio.append(ptramo)
    
    for tramo in range(1, n, 1):
        trazadores_list.append(str(xi[tramo-1])+" <= x <= "+str(xi[tramo]))
    

    return (polinomio, trazadores_list)



# xi = "-1, 0, 3, 4"
# fi = "15.5, 3, 8, 1"


# for i in traza3natural(xi, fi):
#     for j in i:
#         print(j)