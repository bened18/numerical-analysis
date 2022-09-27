%This program finds an interval where f(x) has a sign change
%using the incremental search method

%Inputs:
%f, continuous function
%x0, starting point
%h, pass
%Nmax, maximum number of iterations

%Outputs:
%a, left end of range
%b, right end of range
%iter, number of iterations


function [a,b,iter]=C1_busquedas(f,x0,h,Nmax)

    %initialization
    xant=x0; 
    fant=f(xant);
    xact=xant+h; 
    fact=f(xact);
    
    %Loop
    for i=1:Nmax
        if fant*fact<0
            break;
        end
        xant=xact;
        fant=fact;
        xact=xant+h;
        fact=f(xact);
    end
    
    %Delivery of results
    a=xant;
    b=xact;
    iter=i;
    end