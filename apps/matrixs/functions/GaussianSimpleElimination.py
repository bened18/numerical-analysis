import numpy as np

#Ingreso
a = ([[2, -1, 0, 3],
     [1, 0.5, 3, 8],
     [0, 13, -2, 11],
     [14, 5, -2, 3]])

b = ([[1],
      [1],
      [1],
      [1]])

#procedimiento
#matriz aumentada

M = np.concatenate((a,b), axis=1)
M = M.astype(np.float)
#pivoteo parcial por filas
tamano = np.shape(a)
n = tamano[0]
print(n)

print("Etapa 0");
print(M)
print("")

for i in range(0,n-1,1):
    print("Etapa ", i+1);
    for j in range(i+1,n,1):
        if M[j,i]!=0:
            M[j,i:n+1]=M[j,i:n+1]-(M[j,i]/M[i,i])*M[i,i:n+1]
    print(M)
    print("")

ultfila = n-1;
ultcolumna = n;
x = np.zeros(n,dtype=float);
i = ultfila;
print("Despues de aplicar sustitucion regresiva");
print("x:");
for i in range(ultfila,0-1,-1):
    suma = 0;
    for j in range(i+1,ultcolumna,1):
        suma = suma + M[i,j]*x[j];
    b = M[i,ultcolumna];
    x[i] = (b - suma) / M[i,i];
x = np.transpose([x]);

print(x)