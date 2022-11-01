%This program finds the interpolating polynomial of the given data using the
%Lagrangian method

%Tickets:
%X, abscissa
%Y, ordered

%Departures
%L, Lagrange polynomials
%Coef, coefficients of the interpolation polynomial


function [L,Coef]=C21_lagrange(X,Y) 

    %Inicialización
    n=length(X);
    L=zeros(n);
    
    %Ciclo
    for i=1:n   
        aux0=setdiff(X,X(i));
        aux=[1 -aux0(1)];
        for j=2:n-1
            aux=conv(aux,[1 -aux0(j)]);
        end
        L(i,:)=aux/polyval(aux,X(i));
    end
    
    %Entrega de resultados
    Coef=Y*L;
    end