# Librerías numpy y scipy
from  time  import*
import numpy as np
import pprint
import scipy
import scipy.linalg  

print('MÉTODO LU CON PIVOTEO',end="\n\ n")

print("Este método te halla las matrices L, U y P y cálcula la solución del sistema L * U * X = P * b. Siendo L * U = P * A.\n")

# Coloca la matriz A:
A=np.array([[4,-1,0,3],[1,15.5,3,8],[0,-1.3,-4,1.1],[14,5,-2,30]],float)

# Coloca el vector solución b:
b=np.array([1,1,1,1],float)


t1=perf_counter(); #Calcula tiempo inicio del algoritmo
# Función LU, aquí se inserta la matriz y su tamaño
P, L, U = scipy.linalg.lu(A)
t2=perf_counter(); #Calcula tiempo final del algoritmo

A = np.array(A,float)
P = np.array(P,float)
L = np.array(L,float)
U = np.array(U,float)

print ("Matriz A:")
pprint.pprint(A)
print ("Matriz P:")
pprint.pprint(np.linalg.inv(P))
print ("Matriz L:")
pprint.pprint(L)
print ("Matriz U:")
pprint.pprint(U)
print("\nVector solución b: \n"+str(b))

L = np.dot(P,L)
y = np.linalg.solve(L,b)
print("La solución de Y es:\n" +str(y))

x = np.linalg.solve(U,y)
print("La solución de X es: \n"+str(x))

R = x - np.linalg.solve(A,b)


