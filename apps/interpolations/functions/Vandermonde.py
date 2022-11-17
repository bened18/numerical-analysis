import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
from tabulate import tabulate


xi = [-1,0,3,4]
fi = [15.5,3,8,1]

def vandermonde(xi,fi):
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
  print('Vandermonde: ')
  print((tabulate(D, tablefmt="html")))
  resultado = resultado + (tabulate(D, tablefmt="html"))
  print('Polynomial coefficients: ')
  print(coeficiente)
  print('Interpolation polynomial: ')
  print(polinomio)
  print('\n ')
  sym.pprint(polinomio)