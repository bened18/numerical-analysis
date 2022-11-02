import numpy as np
import math

def cholesky(A):
    n = len(A)
    L = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if (i == j):
                L[i][j] = math.sqrt(A[i][i] - s)
            else:
                L[i][j] = (1.0 / L[j][j] * (A[i][j] - s))
    return L

A = np.array([[4,12,-16],[12,37,-43],[-16,-43,98]])
L = cholesky(A)
print(L)
print(np.dot(L,L.T))


def gauss(A, b):
    n = len(A)
    for row in range(0, n):
        for i in range(row+1, n):
            factor = A[i][row] / A[row][row]
            for j in range(row, n):
                A[i][j] = A[i][j] - factor * A[row][j]
            b[i] = b[i] - factor * b[row]
    x = np.zeros(n)
    x[n-1] = b[n-1] / A[n-1, n-1]
    for row in range(n-2, -1, -1):
        x[row] = (b[row] - np.dot(A[row,row+1:], x[row+1:])) / A[row, row]
    return x



A = np.array([[4,-1,0,3],[1, 15.5, 3, 8], [0,-1.3,-4,1.1], [14, 5, -2, 30]])
b = np.array([1,1,1,1])
x = gauss(A, b)
print(x)