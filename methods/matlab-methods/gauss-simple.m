%This program finds the solution to the system Ax=b using the method of simple Gaussian elimination.

%Inputs:
%A, invertible matrix
%b, constant vector

%Output
%x, solution

function x=C8_gausspl(A,b) 

    %initialization
    n=size(A,1);
    M=[A b];
    
    %We reduce the system
    for i=1:n-1
        for j=i+1:n
            if M(j,i)~=0
               M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
            end
        end
    end
    
    %Delivery of results
    x=sustregr(M); %backward substitution
    end