import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

xi = [0,0.2,0.3,0.4]
fi = [1,1.6,1.7,2.0]
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

    
print('Vandermonde: ')
print(D)
print('Polynomial coefficients: ')
print(coeficiente)
print('Interpolation polynomial: ')
print(polinomio)
print('\n ')
sym.pprint(polinomio)

# Grafica
plt.plot(xi,fi,'o', label='[xi,fi]')
plt.plot(xin,yin, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title(polinomio)
plt.show()