import numpy as np
import math

def doolittle(A):
    n = len(A)
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            s1 = sum(L[i][k] * U[k][j] for k in range(j))
            if (i == j):
                L[i][j] = 1
                U[i][j] = A[i][j] - s1
            else:
                L[i][j] = (1.0 / U[j][j] * (A[i][j] - s1))
                U[i][j] = 0
    return L, U

A = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])
L, U = doolittle(A)
print(L)
print(U)

