def formaMatrizAumentada(A,b):
        import numpy as np
        n = len(A[0])
        det =  np.linalg.det(np.array(A))

        for i in A:
            if n != len(i):
                return A, "La matriz A presenta ecuaciones con más o menos incognitas que otras, por lo tango el sistema es inconsistente y no tiene solucion</br>"
        ranA = np.linalg.matrix_rank(np.matrix(A))
        for a, b in zip(A, b):
            a.append(b)
        ranAb =  np.linalg.matrix_rank(np.matrix(A))
        result = ''
        if ranA == ranAb and ranAb == n:
            result += "El rango de A es igual al rango de la matriz aumentada y el rango de A es igual al numero de incognitas, entonces el sistema es compatible determinado y por esto el sistema tiene solucion unica</br>"
        elif ranA == ranAb and ranAb < n:
            result += f"El rango de A es igual al rango de la matriz aumentada pero el rango de la matriz aumentada es menor al numero de incognitas, entonces el sistema es compatible indeterminado y por esto el sistema tiene infinitas soluciones, además el determinante de la matriz es {det:.5f} y por eso el método no converge</br>"
        else:
            result += "El rango de A es menor al rango de la matriz aumentada, entonces el sistema es incompatible y no tiene solucion</br>"
        return A, result

def sustitucionProgresiva(Lb, n):
        x = [Lb[0][n] / Lb[0][0]]
        while len(x) < n:
            r = 0
            for i in range(len(x)):
                r += Lb[len(x)][i]*x[i]
            r = (Lb[len(x)][n] - r)/Lb[len(x)][len(x)]
            x.append(r)
        return x

def sustitucionRegresiva(Ab, n):
        x = [0 for i in range(n)]
        if Ab[n-1][n-1] == 0:
            return f"</br>Al intentar hacer sustitucion regresiva, se genera una división por 0, lo que indica que el sistema tiene infinitas soluciones</br>" 
        x[n-1] = Ab[n-1][n] / Ab[n-1][n-1]
        for i in range(n-1, -1, -1):
            sumatoria = 0
            for p in range(i+1, n):
                sumatoria += Ab[i][p] * x[p]
            if Ab[i][i] == 0:
                return f"</br>Al intentar hacer sustitucion regresiva, se genera una división por 0, lo que indica que el sistema tiene infinitas soluciones</br>"    
            x[i] = (Ab[i][n] -  sumatoria)/Ab[i][i]
        return x

def infinitasSoluciones(Ab):
        x = []
        x.append("t")
        for i in range(len(Ab)-2,-1,-1):
            result = f"{Ab[i][len(Ab)]}"
            index = len(Ab)-1
            for j in x:
                result += f"-{Ab[i][index]}*{j}"
                index -= 1#
            result = f"({result})/{Ab[i][i]}"
            x.append(result)
        return x[::-1]

def luSimple(A,b):
        html = ""
        etapa = 0

        L = []
        for i in range(len(A)):
            row = []
            for j in range(len(A)):
                if i != j:
                    row.append(0.0)
                else:
                    row.append(1.0)
            L.append(row)
        U = [[0.0 for i in range(len(A))] for j in range(len(A))]
        A = [[float(i) for i in j] for j in A]
        U[0] = [i for i in A[0]]
        def factorizacionLU(A, b, n, etapa, html):
            Ab, html_aux = formaMatrizAumentada(A,b)
            html += f"</br>{html_aux}</br>"                      
            for k in range(n-1):
                for i in range(k+1, n):
                    if Ab[k][k] == 0:
                        html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                        return Ab, html
                    L[i][k] = multiplicador = Ab[i][k] / Ab[k][k]
                    for j in range(k, n+1):
                        Ab[i][j] -= (multiplicador * Ab[k][j])
                etapa += 1
                html += f"</br>Etapa {etapa}</br></br>"
                for i in Ab:
                    result = ""
                    for j in i[:len(Ab)]:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>L:</br>"
                for i in L:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>U:</br>"
                i = Ab[etapa]
                U[etapa] = i[:len(Ab)]
                for i in U:
                    result = ""
                    for j in i:
                        result += f"{j:.10e} "
                    html+=f"{result}</br>"
                html+="</br>"
            return Ab, html

        html=f"</br>LU con gaussiana simple:</br></br>Resultados</br></br>Etapa {etapa}</br></br>"
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html += result+"</br>"
        Ab, html  = factorizacionLU(A,b, len(A),etapa,html)

        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        Lb, result = formaMatrizAumentada(L,b)
        z = sustitucionProgresiva(Lb,len(L))
        Uz, result = formaMatrizAumentada(U,z)
        x = sustitucionRegresiva(Uz,len(U))

        if type(x) == str:    
            html += x
            x = infinitasSoluciones(Ab)
            html+="</br>Ya que el sistema es compatible indeterminado, tiene infinitas soluciones y se puede respresentar con:</br></br>x:</br>"

            for i in x:
                html+=f"{i}</br></br>"
            
            html += "</br>con t = 0</br>x:</br>"

            for i in x:
                fun = eval(f"lambda t:{i}")
                result = fun(0) 
                html+=f"{result:.10f}</br>"

            return html

        html+="</br>Despues de aplicar sustitucion progresiva y regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html