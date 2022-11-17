import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate
import json
import math
from sympy.parsing.sympy_parser import parse_expr


xi = np.array([-1, 0, 3, 4])
fi = np.array([15.5, 3, 8, 1])

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


def newton(xi_str, yi_str):
  
    x = convert_string_to_list(xi_str)
    y = convert_string_to_list(yi_str)
    n = len(x)
    ny=len(y)
    if(n==ny):
      tabla = np.zeros((n+1, n+1))

      for i in range(n):
          tabla[i][0] = x[i]
          tabla[i][1] = y[i]

      res = polinomioNewton(tabla, n)
      return(res)
    else:
      return("the size of the vectors are different")
    # for i in range(len(res)):
    # 	res[i].pop(0)
    # res.pop()
    # return np.array(res).tolist()


def polinomioNewton(tabla, n):
    respuesta = ""
    polinomio = "P(X) = " + str(tabla[0][1])
    F = sym.Function('F')
    for j in range(2, n+1):
        for i in range(j-1, n):
            tabla[i][j] = (tabla[i][j-1] - tabla[i-1][j-1]) / \
                (tabla[i][0] - tabla[i-j+1][0])
            if (i == j-1):
                polinomio += " + " + str(tabla[i][j])
                for i in range(0, i):
                    polinomio += "(x - " + str(tabla[i][0]) + ")"
    respuesta = respuesta + (tabulate(tabla, headers=["xi", "yi", "Primera", "Segunda",
                             "Tercera", "Cuarta", "Quinta", "Sexta", "Septima"], tablefmt="html"))
    respuesta = respuesta + ("\nDiferencias divididas\n")
    for i in range(1, len(tabla)):
        respuesta = respuesta + " | " + str(tabla[i-1][i])
    F = parse_expr(polinomio.replace("P(X) = ", "").replace("(", "*("))
    respuesta = respuesta + ("\nPolinomio interpolante \n" + polinomio)
    return respuesta


newton(np.array([-1, 0, 3, 4]), np.array([15.5, 3, 8, 1]))
