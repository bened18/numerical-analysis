%This program finds the solution to the system Ax=b and the LU factorization of PA
%using the LU factorization method with Gaussian elimination with partial pivoting.

%Tickets:
%A, invertible matrix
%b, constant vector

%Departures
%x, solution
%L, matrix L of the factorization
%U, matrix U of the factorization
%P, permutation matrix


function [x,L,U,P]=C12_lupar(A,b)

    %Inicialización
    n=size(A,1);
    L=eye(n);
    U=zeros(n);
    P=eye(n);
    M=A;
    
    %Factorización
    for i=1:n-1
        %Cambio de filas
        [aux0,aux]=max(abs(M(i+1:n,i)));
        if aux0>abs(M(i,i))
            aux2=M(i+aux,i:n);
            aux3=P(i+aux,:);
            M(aux+i,i:n)=M(i,i:n);
            P(aux+i,:)=P(i,:);
            M(i,i:n)=aux2;
            P(i,:)=aux3;
            if i>1
               aux4=L(i+aux,1:i-1);
               L(i+aux,1:i-1)=L(i,1:i-1);
               L(i,1:i-1)=aux4;
            end
        end
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
    z=sustprgr([L P*b]);
    x=sustregr([U z]);
    end