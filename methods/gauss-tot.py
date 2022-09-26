import numpy as np

def gausstot(A,b):

    n=np.size(A);
    M=np.concatenate(A, b);
    cambi=[];

    for i in range(0,n-1):
        max = 
        fila;
        columna
        #[a,b]=find(abs(M(i:n,i:n))==max(max(abs(M(i:n,i:n)))));
        if b(1)+i-1!=i:
            cambi=[cambi, i b(1)+i-1];
            aux2=M[:,b(1)+i-1];
            M[:,b(1)+i-1]=M[:,i];
            M[:,i]=aux2;
        if a(1)+i-1!=i:
            aux2=M[i+a(1)-1,i:n+1];
            M[a(1)+i-1,i:n+1]=M[i,i:n+1];
            M[i,i:n+1]=aux2;
        for j in range(i+1,n):
            if M[j,i]!=0:
                M[j,i:n+1]=M[j,i:n+1]-(M[j,i]/M[i,i])*M[i,i:n+1];
        print(M)

    x=sustregr(M);
    for i in range(np.size(cambi),1,-1):
        aux=x[cambi(i,1)];
        x[cambi[i,1]]=x[cambi[i,2]];
        x[cambi[i,2]]=aux;