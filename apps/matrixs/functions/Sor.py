import numpy as np
import math

def sor(A, b, w, x, N):
    n = len(A)
    for i in range(N):
        for j in range(n):
            s1 = sum(A[j][k] * x[k] for k in range(j))
            s2 = sum(A[j][k] * x[k] for k in range(j+1, n))
            x[j] = (1-w)*x[j] + (w/A[j][j]) * (b[j] - s1 - s2)
    return x

A = np.array([[4,-1,0,3],[1, 15.5, 3, 8], [0,-1.3,-4,1.1], [14, 5, -2, 30]])
b = np.array([1,1,1,1])
w = 1.5
x = np.array([0,0,0,0])
N = 2
x = sor(A, b, w, x, N)
print(x)