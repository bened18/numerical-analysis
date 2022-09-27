%This program finds the solution to the equation f(x)=0 in the interval [a,b]
%using the false position method

%Inputs:
%f, continuous function
%a, right end of initial interval
%b, end point of end range
%tol, tolerance
%Nmax, maximum number of iterations

%Outputs
%x, solution
%iter, number of iterations
%err, error

function [x,iter,err]=C3_reglafalsa(f,a,b,tol,Nmax)

    %Initialization
    fa=f(a);
    fb=f(b);
    pm=(fb*a-fa*b)/(fb-fa);
    fpm=f(pm);
    E=1000; 
    cont=1;
    
    %Loop
    while E>tol && cont<Nmax
      if fa*fpm<0
         b=pm; 
      else
         a=pm;    
      end 
      p0=pm;
      pm=(f(b)*a-f(a)*b)/(f(b)-f(a));
      fpm=f(pm);
      E=abs(pm-p0);
      cont=cont+1;
    end
    
    %Delivery of results
    x=pm;
    iter=cont;
    err=E;
    end