%This program finds the solution to the system Ax=b using the Jacobi method

%Tickets:
%A, invertible matrix
%b, constant vector
%x0, initial approximation
%tol, tolerance
%Nmax, maximum number of iterations

%Departures
%x, solution
%iter, number of iterations
%err, error


function [x,iter,err]=C16_jacobi(A,b,x0,tol,Nmax)

    %Inicialización
    D=diag(diag(A));
    L=-tril(A)+D;
    U=-triu(A)+D;
    T=inv(D)*(L+U);
    C=inv(D)*b;
    xant=x0;
    E=1000;
    cont=0;
    
    %Ciclo
    while E>tol && cont<Nmax       
        xact=T*xant+C;
        E=norm(xant-xact);
        xant=xact;
        cont=cont+1;
    end
    
    %Entrega de resultados
    x=xact;
    iter=cont;
    err=E;
    end