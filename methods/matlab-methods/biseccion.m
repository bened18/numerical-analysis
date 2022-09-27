%This program finds the solution to the formulation f(x)=0 in the interval [a,b]
%using the bisection method.

%Inputs:
%f, continuous function
%a, right end of initial interval
%b, end point of end range
%tol, tolerance
%Nmax, maximum number of iterations

%Output
%x, solution
%iter, number of iterations
%err, error

function [x,iter,err]=C2_biseccion(f,a,b,tol,Nmax)

    %initialization
    fa=f(a);
    pm=(a+b)/2;
    fpm=f(pm);
    E=1000; 
    cont=1;
    
    %loop
    while E>tol && cont<Nmax
      if fa*fpm<0
         b=pm; 
      else
         a=pm;    
      end
      p0=pm;
      pm=(a+b)/2;
      fpm=f(pm);
      E=abs(pm-p0);
      cont=cont+1;
    end
    
    %Delivery of results
    x=pm;
    iter=cont;
    err=E;
    end