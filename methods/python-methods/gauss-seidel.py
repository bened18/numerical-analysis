import numpy as np

def gaussSeidel(A, b, x, N, tol):
    maxIterations = 1000000 # No modificar
    xprev = [0.0 for i in range(N)]
    for i in range(maxIterations):
        for j in range(N):
            xprev[j] = x[j]
        for j in range(N):
            summ = 0.0
            for k in range(N):
                if (k != j):
                    summ = summ + A[j][k] * x[k]
            x[j] = (b[j] - summ) / A[j][j]
        diff1norm = 0.0
        oldnorm = 0.0
        for j in range(N):
            diff1norm = diff1norm + abs(x[j] - xprev[j])
            oldnorm = oldnorm + abs(xprev[j])  
        if oldnorm == 0.0:
            oldnorm = 1.0
        norm = diff1norm / oldnorm
        if (norm < tol) and i != 0:
            print("\nLa solución converge en x: [", end="")
            for j in range(N - 1):
                print(x[j], ",", end="")
            print(x[N - 1], "]\nLuego de", i + 1, "iteraciones\n")
            return
    print("La matriz no converge.")

# Matriz A
'''A = [[-4.6658333e+01, -8.6801220e+00, -1.6502950e+00],
[0.0, 1.2866580e+00, 5.2480200e-01],
[0.0, 0.0, 3.3315000e-02]]'''
A = np.array((
    (4, -1, 0, 3),
    (1, 15.5, 3, 8),
    (0, -1.3, -4, 1.1),
    (14, 5, -2, 30)
))

# Vector b
'''b = [-10.308984, -1.929987, -0.0]'''
b = [1,1,1,1]

# Xo vector de iteraciòn inicial
v_inicial = [0.0, 0.0, 0.0, 0.0]


print('Matriz A:\n', A.round(6))

print('\nVector b:\n', b)

gaussSeidel(A, b, v_inicial, 2, 1e-7)
