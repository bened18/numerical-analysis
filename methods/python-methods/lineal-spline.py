import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

#ingreso
xi = np.array([-1,0,3,4])
fi = np.array([15.5,3,8,1])

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
    pxsection = pxsection + m*(x-xi[section-1])
    
    px_table.append(pxsection)

#salida
for section in range(1,n,1):
    pxsection = px_table[section-1]
    print(pxsection)

#grafica
samples = 11
xstreak = np.array([])
ystreak = np.array([])
for section in range(1,n,1):
    a = xi[section-1]
    b = xi[section]
    xsection = np.linspace(a,b,samples)
    pxsection = px_table[section-1]
    pxt = sym.lambdify(x,pxsection)
    ysection = pxt(xsection)
    xstreak = np.concatenate((xstreak,xsection))
    ystreak = np.concatenate((ystreak,ysection))

plt.plot(xi,fi, 'ro', label='puntos')
plt.plot(xstreak,ystreak, label='trazador')
plt.show()