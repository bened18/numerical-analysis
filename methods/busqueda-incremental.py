from math import *

funcion = input("ingresa la funcion");
x0 = float(input("ingresa el valor de partida")); 
delta = float(input("ingresa el tamano del intervalo"));            #pedimos datos al usuario
itermax = int(input("ingresa el numero maximo de iteraciones"));

def f(x):                                       
    return eval(funcion);                               #evalua las funciones


def busquedaincremental(x0, delta, itermax):
    
    iteracion = 0;
    x1 = x0 + delta;          #calculamos el delta para evaluar en la funcion                      
    mp =  f(x0) * f(x1);        #miramos si hay cambiio de signo

    while (mp>=0 & iteracion<itermax):      #va a ejecutar el while mientras no haya cambio de signo o no se llegue al limite de iteraciones
        x0 = x1;                            #actualiza el limite inferior del intervalo
        x1 = x0 + delta;                    #actualiza el limite superior del intervalo     
        iteracion = iteracion + 1;
        mp = f(x0) * f(x1);                 #analizamos si hay cambio de signo
        
        print("iteracion" , iteracion, "[",x0,",",x1,"]");      #mostramos la tabla en pantalla

    if mp<0:
        print("el intervalo con posible raiz es [", x0, ",", x1, "]");  
    else:
        print("su llego al limite de iteraciones");
    
    
busquedaincremental(x0,delta,itermax);