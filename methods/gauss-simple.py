import numpy as np
from numpy import array, zeros, fabs, linalg

a = array([[4,2,5],
            [2,5,8],
            [5,4,3]], float);

b = array([[60.7],
            [92.9],
            [56.30]], float);

#a[1] = a[1] - (a[0]/14)*3
print(a)

print("Solution by NumPy:")
print(linalg.solve(a, b))

n = len(b)
x = zeros(n, float)

# first loop specifys the fixed row

##Validar si el primer valor es 0 si es asi no entra al ciclo

for k in range(n-1):

    ##Falta validar si el valor de la diagonal es 0

    # if fabs(a[k, k]) == 0:
    #     for i in range(k+1, n):
    #         if fabs(a[i, k]) > fabs(a[k, k]):
    #             a[[k, i]] = a[[i, k]]
    #             b[[k, i]] = b[[i, k]]
    #             break
 # applies the elimintion below the fixed row
    for i in range(k+1, n):
        if a[i, k] == 0:
            continue

        factor = a[i, k]/a[k, k]
        print(factor)
        a[i] = a[i] - a[k]*factor
        b[i] = b[i] - b[k]*factor
        print(a, b)
print(a)
print(b)


x[n-1] = b[n-1] / a[n-1, n-1]
for i in range(n-2, -1, -1):
    sum_ax = 0

    for j in range(i+1, n):
        sum_ax += a[i, j] * x[j]

    x[i] = (b[i] - sum_ax) / a[i, i]

print("The solution of the system is:")
print(x)
