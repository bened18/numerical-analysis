%This program finds the solution to the equation f(x)=0 using the method of the secant

%Inputs:
%f, continuous function
%x0, initial approximation
%x1, initial approximation
%tol, tolerance
%Nmax, maximum number of iterations

%Output:
%x, solution
%iter, number of iterations
%err, error

function [x,iter,err]=C6_secante(f,x0,x1,tol,Nmax)

    %initialization
    f0=f(x0);
    f1=f(x1);
    E=1000; 
    cont=1;
    
    %Loop
    while E>tol && cont<Nmax
      xact=x1-f1*(x1-x0)/(f1-f0);
      fact=f(xact);
      E=abs(xact-x1);
      cont=cont+1; 
      x0=x1;
      f0=f1;
      x1=xact;
      f1=fact;
    end
    
    %Delivery of results
    x=xact;
    iter=cont;
    err=E;
    end 