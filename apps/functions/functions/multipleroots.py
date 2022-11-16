from math import *
import numpy as np
from tabulate import tabulate


def f(function, x):
  return eval(function)

def df(dfunction, x):
  return eval(dfunction)

def d2f(d2function, x):
  return eval(d2function)

def multipleroot(function, dfunction, d2function, x0,tol,n):
  xant = x0;
  fant = f(function, xant);
  e_abs=1000;
  iteration = 0;
  resultados =[[iteration,xant,f(function, xant),""]]
  
  while iteration<=n:
    xact = xant - fant * df(dfunction, xant) / ((df(dfunction, xant))**2 - fant * d2f(d2function, xant));
    fact = f(function, xact);
    e_abs = abs(xact-xant);
    iteration += 1;
    xant = xact;
    fant = fact;
    resultados.append([iteration,xant,f(function, xant),e_abs])    
    
    if e_abs<tol:
      return (f"Solution found in X = {xact}, iterations:  {iteration-1}  error = {e_abs}", tabulate(resultados, headers=["iter", "Xi", "f(x)", "error"], tablefmt="html"))
  
  if iteration > n:
    return("Solution not found for tolerance = ", tol);
  return()

#root(f,df,d2f,1,10**-7,100);