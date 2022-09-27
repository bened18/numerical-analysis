%This program finds the solution to the system Ax=b using the method of Gaussian elimination with partial pivoting.

%Inputs:
%A, invertible matrix
%b, constant vector

%Output
%x, solution

function x=C9_gausspar(A,b) 

    %initialization
    n=size(A,1);
    M=[A b];
    
    %We reduce the system
    for i=1:n-1
        %Change of rows
        [aux0,aux]=max(abs(M(i+1:n,i)));
        if aux0>abs(M(i,i))
            aux2=M(i+aux,i:n+1);
            M(aux+i,i:n+1)=M(i,i:n+1);
            M(i,i:n+1)=aux2;
        end
        for j=i+1:n
            if M(j,i)~=0
               M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
            end
        end
    end
    
    %Delivery of results
    x=sustregr(M); %backward substitution
    end