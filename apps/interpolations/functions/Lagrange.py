import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def lagrange():
    xi = np.array([-1,0,3,4])
    fi = np.array([15.5,3,8,1])

    n = len(xi)
    x = sym.Symbol('x')
    polinomio = 0
    divisorL = np.zeros(n, dtype = float)
    for i in range(0,n,1):
        
        numerador = 1
        denominador = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerador = numerador*(x-xi[j])
                denominador = denominador*(xi[i]-xi[j])
        terminoLi = numerador/denominador

        polinomio = polinomio + terminoLi*fi[i]
        divisorL[i] = denominador

    polisimple = polinomio.expand()

    px = sym.lambdify(x,polisimple)

    muestras = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,muestras)
    pfi = px(pxi)

    print('    fi values: ',fi)
    print('dividers L(i): ',divisorL)
    print()
    print('Lagrange polynomial, expressions')
    print(polinomio)
    print()
    print('Lagrange polynomial ')
    print(polisimple)

    # plt.plot(xi,fi,'o', label = 'Point')
    # plt.plot(pxi, pfi, label = 'Polynomial')
    # plt.legend()
    # plt.xlabel('xi')
    # plt.ylabel('fi')
    # plt.title('Lagrange interpolation')
    # plt.show()