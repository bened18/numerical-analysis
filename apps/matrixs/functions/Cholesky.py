import numpy as np
from cmath import sqrt
from prettytable import PrettyTable

stages = []
def sustProg(L, b, n):
    if (L[0][0] == 0):
        return
    else:
        z = np.zeros(n, dtype=complex)
        suma3 = 0
        z[0] = b[0][0]/L[0][0]
        for k in range(1, n):
            if (L[k][k] == 0):
                return("Element", k, " in L diagonal, is zero")
                
            else:
                for r in range(k):
                    suma3 = suma3+(L[k][r]*z[r])
                z[k] = (b[k][0]-suma3)/L[k][k]
                suma3 = 0
    return z


def sustRegr(U, z, n):
    if (U[0][0] == 0):
        return
    else:
        x = np.zeros(n, dtype=np.complex)
        suma4 = 0
        x[n-1] = z[n-1]/U[n-1][n-1]
        for k in range(n-2, -1, -1):
            if U[k][k] == 0:
                print("Element", k, " in U diagonal, is zero")
                return
            else:
                suma4 = 0
                for r in range(k+1, n):
                    suma4 = suma4+(U[k][r]*x[r])
                x[k] = (1/U[k][k])*(z[k]-suma4)
    return x

def cholesky(A):
    n = len(A)
    
    #L = np.zeros((n,n), dtype=np.complex_)
    #U = np.zeros((n,n), dtype=np.complex_)
    L = [[0 for j in range(n)] for i in range(n)]
    U = [[0 for j in range(n)] for i in range(n)]
    for i, j in zip(range(n), range(n)): U[i][j] = 1
    for i, j in zip(range(n), range(n)): L[i][j] = 1

    for k in range(n):
        suma1 = 0
        for p in range(0,k):
            suma1 += L[k][p]*U[p][k]
        L[k][k] = sqrt(A[k][k]-suma1) #Complex number handled
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
        print("\nStage ",  k+1, ":" )
        stage = f"<br> <b>Stage {k+1}: </b> <br>"
        stages.append(stage)

        print("\nMatrix L:")
        matrix = f"<b>Matrix L</b><br>"
        stages.append(matrix)
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in L:
            stages.append(table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row]))
        print(table)
        
        print("\nMatrix U:")
        matrix = f"<b>Matrix U</b><br>"
        stages.append(matrix)
        table = PrettyTable()
        table.field_names = [f"x{i}" for i in range(n)]
        for row in U:
            stages.append(table.add_row(['({0.real:.4f} + {0.imag:.2f}i)'.format(i) for i in row]))
        print(table)
    return L,U,

#Fill matrix
def entradas(A,b):
    L,U = cholesky(A)
    n = len(A)

    #Apply sustitution
    z=sustProg(L,b,n)
    x=sustRegr(U,z,n)

    #Show answer
    # ans = []
    # ans.append(['{0.real:.4f}'.format(i) for i in x])
    # print("\nAnswer: ")
    # print(ans)
    return(f"<br><br><b>Input: (matrix)</b> <br> {np.dot(L,U)}".replace("\n", "<br>"), stages)

