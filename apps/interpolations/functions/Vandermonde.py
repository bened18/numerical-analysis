import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate
import json



xi = [-1,0,3,4]
fi = [15.5,3,8,1]

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

def vandermonde(x,f):
  muestras = 101
  xi = np.array(xi)
  B = np.array(fi)
  n = len(xi)
  D = np.zeros(shape=(n,n),dtype =float)
  for i in range(0,n,1):
      for j in range(0,n,1):
          potencia = (n-1)-j
          D[i,j] = xi[i]**potencia

  coeficiente = np.linalg.solve(D,B)

  x = sym.Symbol('x')
  polinomio = 0
  for i in range(0,n,1):
      potencia = (n-1)-i  
      termino = coeficiente[i]*(x**potencia)
      polinomio = polinomio + termino

  px = sym.lambdify(x,polinomio)

  a = np.min(xi)
  b = np.max(xi)
  xin = np.linspace(a,b,muestras)
  yin = px(xin)

  resultado = ""
  #print('Vandermonde: ')
  #print((tabulate(D, tablefmt="html")))
  resultado = resultado + (tabulate(D, tablefmt="html"))
  #print('Polynomial coefficients: ')
  resultado = resultado +'\nPolynomial coefficients: \n'
  resultado = resultado +str(coeficiente)
  #print(coeficiente)
  #print('Interpolation polynomial: ')
  resultado = resultado +'\nInterpolation polynomial: \n'
  resultado = resultado + str(polinomio)
  #print(polinomio)
  #print('\n ')
  #sym.pprint(polinomio)
  print(resultado)

# GRAFICACION DEL EJERCICIO
# --------------------------------------------
# plt.plot(xi,fi,'o', label='[xi,fi]')
# plt.plot(xin,yin, label='p(x)')
# plt.xlabel('xi')
# plt.ylabel('fi')
# plt.legend()
# plt.title(polinomio)
# plt.show()
# --------------------------------------------

vandermonde(xi,fi)