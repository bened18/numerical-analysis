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

def cholesky(A):
    n = len(A)
    L,U = inicializa(n,2)
    epochs = []

    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1)
        U[k][k] = L[k][k]
        for i in range(k,n):
            suma2 = 0
            for p in range(k):
                suma2+=L[i][p]*U[p][k]
            L[i][k] = (A[i][k]-suma2)/(U[k][k])
        for j in range(k+1,n):
            suma3 = 0
            for p in range(k):
                suma3+= L[k][p]*U[p][j]
            U[k][j]= (A[k][j]-suma3)/(L[k][k])
            
        epoch = f"Epoch {k}: <br>"
        epochs.append(epoch)
        
        matrix = f"Matrix L<br>"
        epochs.append(matrix)
        values_matrix = f"{L}<br>"
        epochs.append(values_matrix)
        
        matrix2 = f"<br>Matrix U<br>"
        epochs.append(matrix2)
        values_matrix2 = f"{U}<br>"
        epochs.append(f"{values_matrix2}<br>")
        
    return(epochs, f"<br><br>Test: (matrix) <br> {np.dot(L,U)}".replace("\n", "<br>"))
    
# K = [[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]] 
# cholesky(K)