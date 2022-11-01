%This program finds the solution to the system Ax=b and the LU factorization of A
%using Doolittle's method

%Tickets:
%A, invertible matrix
%b, constant vector

%Departures
%x, solution
%L, matrix L of the factorization
%U, matrix U of the factorization

function [x,L,U]=C14_Doolittle(A,b)

    %Inicialización
    n=size(A,1);
    L=eye(n); 
    U=eye(n);
    
    %Factorización
    for i=1:n-1
        for j=i:n
            U(i,j)=A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)');
        end
        for j=i+1:n
            L(j,i)=(A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)'))/U(i,i);
        end
    end
    U(n,n)=A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)');
    
    %Entrega de resultados
    z=sustprgr([L b]);
    x=sustregr([U z]);     
    end