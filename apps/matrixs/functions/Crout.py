from cmath import sqrt
import numpy as np

def inicializa(n,metodo):
    L , U = [] , []
    if metodo == 0:
        L = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
        U = [[0 for j in range(n)] for i in range(n)]
    elif metodo == 1:
        L = [[0 for j in range(n)] for i in range(n)]
        U = [[1 if j == i else 0 for j in range(n)] for i in range(n)]
    elif metodo == 2:
        L = [[0 for j in range(n)] for i in range(n)]
        U = [[0 for j in range(n)] for i in range(n)]
    return L , U

def crout(A,n):
    L,U = inicializa(n,1)

    for k in range(n):
        suma1 = 0.0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = A[k][k] - suma1
        for i in range(k+1,n):
            suma2 = 0.0
            for p in range(k):
                suma2 += L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0.0
            for p in range(k):
                suma3 += L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
        print("\nEtapa ",  k )
        print("\nL:\n")
        print(L)
        print("\nU:\n")
        print(U)#imprimir L  U y k etapa
    print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(L,U))
    return L,U


K = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]]
n = 4

crout(K,n)