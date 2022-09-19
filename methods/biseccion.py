from math import *

funcion = input("ingrese la funcion ");
a = float(input("ingrese la cota inferior "));                              #pedimos los datos al usuario
b = float(input("ingrese la cota superior "));
tol = float(input("ingrese la tolerancia deseada "));

def f(x):
        return eval(funcion);                               #esta funcion retorna la ecuacion evaluada
    
def biseccion(a,b,tol):
    
    m1=a; 
    m=b; 
    iteracion = 0;

    if((f(a) * f(b)) > 0):                      
        print("la funcion no cambia de signo");             #validamos que la funcion cambie de signo en el intervalo dado
    
    while(abs(m1-m)>tol):
        m1=m; 
        m=(a+b)/2;                                          #punto medio del intervalo
        
        if((f(a)*f(m))<0):                                  #si en el limite inferior hay cambio de signo 
            b=m;                                            #entonces m sera el nuevo limite superior
        
        if((f(m)*f(b))<0):                                  #si en el limite superior hay cambio de signo
            a=m;                                            #entonces m sera el nuevo limite inferior
        
        error = abs((m1-m)/m1);                         
        iteracion = iteracion + 1;
        
        print("iteracion ", iteracion, "el intervalo es [",a,",",b,"] y el error es = ", error);    #imprimimos la tabla
        
    print("En la iteracion",iteracion,"se obtiene que",m,"es una buena aproximacion");              #se da el resultado final

biseccion(a,b,tol);                     