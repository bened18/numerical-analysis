import numpy as np

def crout(A):

    L = np.zeros((3, 3))
    U = np.zeros((3, 3))

    for k in range(0, 3):
      U[k, k] = 1 
      for j in range(k, 3):
            sum0 = sum([L[j, s] * U[s, k] for s in range(0, k)])  
            L[j, k] = A[j, k] - sum0 

      for j in range(k+1, 3):
            sum1 = sum([L[k, s] * U[s, j] for s in range(0, k)]) 
            U[k, j] = (A[k, j] - sum1) / L[k, k]



      print(L)
      print()
      print(U)
      return L, U

A = np.array([[60.0, 30.0, 20.0], [30.0, 20.0, 15.0], [20.0, 15.0, 12.0]])
crout(A)