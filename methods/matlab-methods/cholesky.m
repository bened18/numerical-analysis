%This program finds the solution to the system Ax=b and the LU factorization of A
%using Cholesky's method

%Tickets:
%A, invertible matrix
%b, constant vector

%Departures
%x, solution
%L, matrix L of the factorization
%U, matrix U of the factorization


function [x,L,U]=C15_Cholesky(A,b)

    %Inicialización
    n=size(A,1);
    L=eye(n); 
    U=eye(n);
    
    %Factorización
    for i=1:n-1
        L(i,i)=sqrt(A(i,i)-dot(L(i,1:i-1),U(1:i-1,i)'));
        U(i,i)=L(i,i);
        for j=i+1:n
            L(j,i)=(A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)'))/U(i,i);
        end
        for j=i+1:n
            U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
        end
    end
    L(n,n)=sqrt(A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)'));
    U(n,n)=L(n,n);
    
    %Entrega de resultados
    z=sustprgr([L b]);
    x=sustregr([U z]);       
    end