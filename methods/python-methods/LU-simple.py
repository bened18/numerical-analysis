import numpy as np


m = [[4,-1,0,3],[1, 15.5, 3, 8], [0,-1.3,-4,1.1], [14, 5, -2, 30]]
matriz = np.zeros([m,m])
u = np.zeros([m,m])
l = np.zeros([m,m])

for r in range(0,m):
    for c in range(0,m):
        matriz[r,c]=(input("Elemento a[" + str(r+1) + "," + str(c+1) + "]"))
        matriz[r,c]=float(matriz[r,c])
        u[r,c]=matriz[r,c]


for k in range (0,m):
    
    for r in range(0,m):
        if (k == r):
            l[k,r]=1
        if (k<r):
            factor=(matriz[r,k]/matriz[k,k])
            l[r,k]=factor
            for c in range (0,m):
                matriz[r,c]=matriz[r,c]-(factor*matriz[k,c])
                u[r,c]=matriz[r,c]
    print("\nEtapa ",  k, ":" )
    print("\nMatriz L")
    print(l)
    print("\nMatriz U")
    print(u)  
print ("\n\n\n Prueba: (analiza con la matriz ingresada)\n", np.dot(l,u))