from math import *

funcion = input("ingresa la funcion");
x0 = float(input("ingresa el valor de partida")); 
tol = float(input("ingresa la tolerancia"));            #pedimos datos al usuario
itermax = int(input("ingresa el numero maximo de iteraciones"));

def g(x):
    return eval(funcion);           #evalua las funciones

def punto_fijo(x0, tol, itermax):   #pedimos valor inical, tolerancia e iteraciones maximas
    iter = 1;
    while iter<=itermax:            #mientras tengamos iteraciones disponibles
       
        x1 = g(x0);                 #evaluamos la funcino con el punto anterior   
        error = abs((x1-x0)/x1);    #error absoluto
        print("iteracion", iter, "punto", iter, "funcion", x1, "error", error); #imprimimos la tabla
        
        if error < tol:             #si llegamos a la tolerancia deseada paramos
            print("solucion encontrada en la iteracion", iter, "con x=", x1 );
            return x1
        
        x0 = x1;                #guardamos el valor actual
        iter += 1               #aumentamos iteracion
    
    print("solucion no encontrada, iteraciones agotadas: ", iter);  #si se sale del while
    return None;

punto_fijo(x0, tol, itermax);
        