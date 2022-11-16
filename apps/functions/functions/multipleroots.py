from math import *
import numpy as np
from tabulate import tabulate


def f(x):
  return np.exp(x) - x - 1;

def df(x):
  return np.exp(x) - 1;

def d2f(x):
  return np.exp(x);

def multipleroot(x0,tol,n):
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
      return (f"Solution found in X = {xact}, iterations:  {iteration-1}  error = {e_abs}", tabulate(resultados, headers=["iter", "Xi", "f(x)", "error"], tablefmt="html"))
  
  if iteration > n:
    return("Solution not found for tolerance = ", tol);
  return()

#root(f,df,d2f,1,10**-7,100);