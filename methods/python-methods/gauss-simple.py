import numpy as np

#Ingreso
a = ([[4,2,5],
     [2,5,8],
     [5,4,3]])

b = ([[60.7],
      [92.9],
      [56.30]])

#procedimiento
#matriz aumentada

M = np.concatenate((a,b), axis=1)
M = M.astype(np.float)
#pivoteo parcial por filas
tamano = np.shape(a)
n = tamano[0]
print(n)

print(M)
print("")

for i in range(0,n-1,1):
    for j in range(i+1,n,1):
        if M[j,i]!=0:
            M[j,i:n+1]=M[j,i:n+1]-(M[j,i]/M[i,i])*M[i,i:n+1]
    print(M)
    print("")

ultfila = n-1;
ultcolumna = n;
x = np.zeros(n,dtype=float);
i = ultfila;
for i in range(ultfila,0-1,-1):
    suma = 0;
    for j in range(i+1,ultcolumna,1):
        suma = suma + M[i,j]*x[j];
    b = M[i,ultcolumna];
    x[i] = (b - suma) / M[i,i];
x = np.transpose([x]);

print(x)