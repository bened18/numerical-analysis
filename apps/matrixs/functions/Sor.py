from math import fabs

def normaInfVector(L):
    """ Calcula la norma infinita de un vector:
            ||x|| = max {|xi|}, i = 0, 1, ... n.
    """

    maximum = fabs(L[0])
    for i in range(1, len(L)):
        maximum = max(maximum, fabs(L[i]))
    return maximum


def sor(A, b, tol, w):

    n = len(A)
    Xk = [0.0]*n
    sumation = 0.0
    for i in range(n):
        if A[i][i] == 0:
            exit('Los elementos A[i][i] deben ser diferentes de 0')

    Xk1 = [b[i]/float(A[i][i]) for i in range(n)]
    def minus(x, y): return [x[i]-y[i] for i in range(n)]

    for j in range(n):
        dominancia = 0.0
        for i in range(n):
            if j != i:
                dominancia += fabs(A[i][j])
        if A[i][i] < dominancia:
            exit('La matriz no converge')
    iter = 1
    while (normaInfVector(minus(Xk1, Xk)) / float(normaInfVector(Xk1))) > tol:
        Xk[:] = Xk1[:]
        print(iter)
        for i in range(n):
            sumation1 = sum(A[i][j]*Xk1[j] for j in range(i))
            sumation2 = sum(A[i][j]*Xk1[j] for j in range(i+1, n))
            err = (normaInfVector(minus(Xk1, Xk)) / float(normaInfVector(Xk1)))
            Xk1[i] = (float(w)/A[i][i]) * \
                (b[i] - sumation1 - sumation2) + (1-w)*Xk[i]
        iter += 1    
        print("error", err)
        print("que es esto", Xk1)
    return Xk1





A = [[4, -1,   0,  3],
     [1, 15.5, 3,  8],
     [0, -1.3, -4, 1.1],
     [14, 5,   -2, 30]]
b = [1, 1, 1, 1]
tol = 1e-7
w = 1.5
sor(A, b, tol, w)