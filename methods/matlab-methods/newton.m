%This program finds the solution to the equation f(x)=0 using the method of Newton

%Inputs:
%f, continuous function
%f', continuous function
%x0, initial approximation
%tol, tolerance
%Nmax, maximum number of iterations

%Outputs:
%x, solution
%iter, number of iterations
%err, error


function [x,iter,err]=C5_newton(f,df,x0,tol,Nmax)

    %Initialization
    xant=x0;
    fant=f(xant);
    E=1000; 
    cont=0;
    
    %Loop
    while E>tol && cont<Nmax
      xact=xant-fant/(df(xant));
      fact=f(xact);
      E=abs(xact-xant);
      cont=cont+1;
      xant=xact;
      fant=fact;
    end
    
    %Delivery of results
    x=xact;
    iter=cont;
    err=E;
    end 