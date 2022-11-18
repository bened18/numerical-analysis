import numpy as np
import pprint


def jacobi(a,b,x): 
	n=len(x) 
	t=x.copy()
	for  i  in  range(n): 
		s=0
		for j in range(n): 
			if i!=j:
				s=s+a[i,j]*t[j]
				x[i]=(b[i]-s)/a[i,i]
	return x


def jacobim(a,b,x,e,m): 
	n=len(x)  
	t=x.copy()
	print ("Para la iteración "+str(0)+": X = "+"0.0      0.0  0.0       0.0"+"\tError: "+ " ")
	for  k  in  range(m): 
		x=jacobi(a,b,x)
		d=np.linalg.norm(np.array(x)-np.array(t),np.inf)
		print ("Para la iteración "+str(k+1)+": X = "+str(np.transpose(x.round(7)))+"\tError: "+str(abs(d)))
		if d<e:
			return [x,k] 
		else:
			t=x.copy() 
	return [[],m]

# Matriz a usar
A = np.array([[4,-1,0,3],[1, 15.5, 3, 8], [0,-1.3,-4,1.1], [14, 5, -2, 30]],float)

# Vector Solución
b = np.array([[1],[1],[1],[1]],float)

# Vector de Inicio
x=np.array([[0],[0],[0],[0]],float)

# Numéro de iteraciones
maxite=1000

print ("\nMatriz A:")
pprint.pprint(A)
print ("\nVector b:")
pprint.pprint(b)

print("")

# X es la solución y k las iteraciones
[x,k]=jacobim(A,b,x,1.e-7,100)

if(k==maxite):
	print("\nEl método diverge o no converge para la cota de error pedido")

else: 
	print("\nEl vector 'x' es:")
	print(x)

	print("\nEl numero de iteraciones es: "+str(k+1))