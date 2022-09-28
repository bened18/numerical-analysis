from math import *
import numpy as np
from tabulate import tabulate


def f(x):
  return np.exp(x) - x - 1;

def df(x):
  return np.exp(x) - 1;

def d2f(x):
  return np.exp(x);

def root(f,df,d2f,x0,tol,n):
  xant = x0;
  fant = f(xant);
  e_abs=1000;
  iteration = 0;
  resultados =[[iteration,xant,f(xant),""]]
  
  while iteration<=n:
    xact = xant - fant * df(xant) / ((df(xant))**2 - fant * d2f(xant));
    fact = f(xact);
    e_abs = abs(xact-xant);
    iteration += 1;
    xant = xact;
    fant = fact;
    resultados.append([iteration,xant,f(xant),e_abs])    
    
    if e_abs<tol:
      print("Solution found in X =", xact, "     iterations:", iteration-1, "    error =", e_abs);
      break;
  
  if iteration > n:
    print("Solution not found for tolerance = ", tol);
  print(tabulate(resultados, headers=["iter", "Xi", "f(x)", "error"], tablefmt="github"))

root(f,df,d2f,1,10**-7,100);