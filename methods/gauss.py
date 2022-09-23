import numpy as np

#Ingreso
a = ([[4,2,5],
     [2,5,8],
     [5,4,3]]);

b = ([[60.7],
      [92.9],
      [56.30]]);

#procedimiento
#matriz aumentada

ab = np.concatenate((a,b), axis=1);
ab0 = np.copy(ab);

#pivoteo parcial por filas
tamano = np.shape(ab);
n = tamano[0];
m = tamano[1];

#para cada fila en AB
for i in range (0,n-1,1):
    #columna desde diagonal i en adelante
    columna = abs(ab[i:,i]);
    dondemax = np.argmax(columna);
    
    #dondemax no esta en diagonal
    if (dondemax != 0):
        #intercambia filas
        temporal = np.copy(ab[i,:]);
        ab[i,:] = ab[dondemax+i, :];
        ab[dondemax+i,:] = temporal;
ab1 = np.copy(ab);
        
#eliminacion por filas
for i in range(0,n-1,1):
    
    pivote = ab[i,i];
    adelante = i+1;
    for k in range (adelante,n,1):
        factor = ab[k,i]/pivote;
        ab[k,:] = ab[k,:] - ab[i,:]*factor;

#sustitucion hacia atras
ultfila = n-1;
ultcolumna = m-1;
x = np.zeros(n,dtype=float);
i = ultfila;
for i in range(ultfila,0-1,-1):
    suma = 0;
    for j in range(i+1,ultcolumna,1):
        suma = suma + ab[i,j]*x[j];
    b = ab[i,ultcolumna];
    x[i] = (b - suma) / ab[i,i];
x = np.transpose([x]);
#salida
print('Matriz aumentada');
print(ab0);
print('pivoteo parcial por filas');
print(ab1);
print('eliminacion hacia adelante');
print(ab)
print('solucion buscada');
print(x);
print('verificacion');
print(np.dot(a,x));