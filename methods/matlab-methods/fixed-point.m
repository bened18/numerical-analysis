%This program finds the solution to the equation f(x)=0 by solving the problem
%analog x=g(x) using the fixed point method.

%Inputs:
%f, continuous function
%g, continuous function
%x0, initial approximation
%tol, tolerance
%Nmax, maximum number of iterations

%Outputs
%x, solution
%iter, number of iterations
%err, error


function [x,iter,err]=C4_puntofijo(g,x0,tol,Nmax)

    %initialization
    xant=x0;
    E=1000; 
    cont=0;
    
    %Loop
    while E>tol && cont<Nmax
      xact=g(xant);
      E=abs(xact-xant);
      cont=cont+1;
      xant=xact;
    end
    
    %Delivery of results
    x=xact;
    iter=cont;
    err=E;
    end