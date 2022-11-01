%This program finds the interpolating polynomial of the given data using the
%divided difference method

%Tickets:
%X, abscissa
%Y, ordered

%Departures
%Coef, coefficients of the Newton polynomial


function Coef=C20_difdivididas(X,Y)

  %Inicialización
  n=length(X);
  D=zeros(n);
  
  %Ciclo
  D(:,1)=Y';
  for i=2:n
      aux0=D(i-1:n,i-1);
      aux=diff(aux0);
      aux2=X(i:n)-X(1:n-i+1);
      D(i:n,i)=aux./aux2';
  end
  
  %Entrega de resultados
  Coef=diag(D)';
  end