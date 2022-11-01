%This program finds the solution to the system Ax=b and the LU factorization of A
%using the LU factorization method with simple Gaussian elimination.

%Tickets:
%A, invertible matrix
%b, constant vector

%Departures
%x, solution
%L, matrix L of the factorization
%U, matrix U of the factorization

function [x,L,U]=C11_lusimpl(A,b)

    %Inicialización
    n=size(A,1);
    L=eye(n);
    U=zeros(n);
    M=A;
    
    %Factorización
    for i=1:n-1
        for j=i+1:n
            if M(j,i)~=0
               L(j,i)=M(j,i)/M(i,i);
               M(j,i:n)=M(j,i:n)-(M(j,i)/M(i,i))*M(i,i:n);           
            end
        end
        U(i,i:n)=M(i,i:n);
        U(i+1,i+1:n)=M(i+1,i+1:n);
    end
    U(n,n)=M(n,n);
    
    %Entrega de resultados
    z=sustprgr([L b]);
    x=sustregr([U z]);
    end