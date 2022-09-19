from math import *

funcion = input("ingrese la funcion ");
a = float(input("ingrese la cota inferior "));
b = float(input("ingrese la cota superior "));
tol = float(input("ingrese la tolerancia deseada "));

def f(x):
        return eval(funcion);
    
def biseccion(a,b,tol):
    
    m1=a; 
    m=b; 
    iteracion = 0;

    if((f(a) * f(b)) > 0):
        print("la funcion no cambia de signo");
    
    while(abs(m1-m)>tol):
        m1=m; #2
        m=(a+b)/2; #1.5
        if((f(a)*f(m))<0):
            b=m;
        if((f(m)*f(b))<0):
            a=m;
        error = abs((m1-m)/m1);
        iteracion = iteracion + 1;
        print("iteracion ", iteracion, "el intervalo es [",a,",",b,"] y el error es = ", error);
        
    print("En la iteracion",iteracion,"se obtiene que",m,"es una buena aproximacion");

biseccion(a,b,tol);
# biseccion(1, 2, 10**(-6));
