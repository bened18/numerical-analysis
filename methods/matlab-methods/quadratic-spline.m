
%This program finds the quadratic spline that interpolates the given data using the
%square plotter method

%Tickets:
%X, abscissa
%Y, ordered

%Departures
%Coef, tracer coefficients


function Coef=C23_trazcuad(X,Y)

    %Inicialización
    n=length(X);
    m=3*(n-1);
    A=zeros(m); 
    b=zeros(m,1);
    Coef=zeros(n-1,3);
    
    %Ciclos
    %Condiciones de interpolación
    for i=1:n-1
        A(i+1,3*i-2:3*i)=[X(i+1)^2 X(i+1) 1];
        b(i+1)=Y(i+1);
    end
    A(1,1:3)=[X(1)^2 X(1)^1 1];
    b(1)=Y(1);
    %Condiciones de continuidad
    for i=2:n-1
        A(n-1+i,3*i-5:3*i)=[X(i)^2 X(i) 1 -X(i)^2 -X(i) -1];
        b(n-1+i)=0;
    end
    %Condiciones de suavidad
    for i=2:n-1
        A(2*n-3+i,3*i-5:3*i)=[2*X(i) 1 0 -2*X(i) -1 0];
        b(2*n-3+i)=0;
    end
    %Condición de frontera
    A(m,1)=2;
    b(m)=0;
    
    %Entrega de resultados
    Saux=A\b;
    %Se organiza la matriz de salida
    for i=1:n-1
        Coef(i,:)=Saux(3*i-2:3*i);
    end
    end