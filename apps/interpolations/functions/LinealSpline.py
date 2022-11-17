import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import json


#ingreso
xi = "-1,0,3,4"
fi = "15.5,3,8,1"


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

def lineal_spline(xi_str,yi_str):
  xi = np.array(convert_string_to_list(xi_str))
  fi = np.array(convert_string_to_list(yi_str))

  resultado = ""
  #procedimiento
  n = len(xi)
  x = sym.Symbol('x')
  px_table = []
  section = 1
  for section in range(1,n,1):
      numerator = fi[section]-fi[section-1]
      denominator = xi[section]-xi[section-1]
      m = numerator/denominator
      pxsection = fi[section-1]
      pxsection = m*(x-xi[section-1]) + pxsection 
      px_table.append(pxsection )

  #salida
  for section in range(1,n,1):
      pxsection = px_table[section-1]
      resultado = resultado + str(pxsection) + "\n"
      #print(pxsection)
  #print(px_table)
  return(resultado)


#GRAFICACION DEL EJERCICIO 
# -----------------------------------------------
# samples = 11
# xstreak = np.array([])
# ystreak = np.array([])
# for section in range(1,n,1):
#     a = xi[section-1]
#     b = xi[section]
#     xsection = np.linspace(a,b,samples)
#     pxsection = px_table[section-1]
#     pxt = sym.lambdify(x,pxsection)
#     ysection = pxt(xsection)
#     xstreak = np.concatenate((xstreak,xsection))
#     ystreak = np.concatenate((ystreak,ysection))

# plt.plot(xi,fi, 'ro', label='puntos')
# plt.plot(xstreak,ystreak, label='trazador')
# plt.show()
# -----------------------------------------------
