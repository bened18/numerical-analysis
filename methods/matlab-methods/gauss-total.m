%This program finds the solution to the system Ax=b using the method of
%Gaussian elimination with total pivoting.

%Inputs:
%A, invertible matrix
%b, constant vector

%Output
%x, solution

function x=C10_gausstot(A,b) 

    %Initialization
    n=size(A,1);
    M=[A b];
    cambi=[];
    
    %We reduce the system
    for i=1:n-1
        [a,b]=find(abs(M(i:n,i:n))==max(max(abs(M(i:n,i:n)))));
        % Column Change
        if b(1)+i-1~=i
            cambi=[cambi; i b(1)+i-1];
            aux2=M(:,b(1)+i-1);
            M(:,b(1)+i-1)=M(:,i);
            M(:,i)=aux2;
        end   
        %change rows
        if a(1)+i-1~=i
            aux2=M(i+a(1)-1,i:n+1);
            M(a(1)+i-1,i:n+1)=M(i,i:n+1);
            M(i,i:n+1)=aux2;
        end
        for j=i+1:n
            if M(j,i)~=0
               M(j,i:n+1)=M(j,i:n+1)-(M(j,i)/M(i,i))*M(i,i:n+1);
            end
        end
    end
    
    %Delivery of results
    x=sustregr(M); %back substitution
    %reorder the solution vector
    for i=size(cambi,1):-1:1
        aux=x(cambi(i,1));
        x(cambi(i,1))=x(cambi(i,2));
        x(cambi(i,2))=aux;
    end
    end