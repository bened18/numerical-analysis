def eliminacionSimple(A,b):
        html="</br>Eliminacion gaussiana simple</br></br>"

        Ab, html = eliminacion(A,b,len(A),html)
        
        if "diagonal" in html:
            return html
        
        if "no tiene solucion" in html:
            return html

        x = sustitucionRegresiva(Ab, len(A))
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

        html+="</br>Despues de aplicar sustitucion regresiva</br></br>x:</br>"

        for i in x:
            html+=f"{i}</br>"

        return html
    
    
def eliminacion(A, b, n, html):
        Ab, html_aux = formaMatrizAumentada(A,b)
        html += f"</br>{html_aux}</br>"
        html+="Resultados</br></br>"
        etapa = 0
        html+=f"Etapa {etapa}</br></br>"
        etapa += 1
        for i in A:
            result = ""
            for j in i:
                result += f"{j:.10e} "
            html += result+"</br>"
        for k in range(n-1):
            for i in range(k+1, n):
                if Ab[k][k] == 0.0:
                    html += f"</br>se ha encontrado un 0 en la diagonal, en la posicion {k+1},{k+1} el método se suspende por una division por 0</br>"
                    return Ab, html
                multiplicador = Ab[i][k] / Ab[k][k]
                for j in range(k, n+1):
                    Ab[i][j] -= (multiplicador * Ab[k][j])
            html+=f"</br>Etapa {etapa}</br></br>"
            for i in Ab:
                result = ""
                for j in i:
                    result += f"{j:.10e} "
                html+=result+"</br>"
            etapa += 1
        return Ab, html

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
        result = 'Utilizando el teorema de Rouché-Frobenius revisar en: <a href="https://es.wikipedia.org/wiki/Teorema_de_Rouch%C3%A9%E2%80%93Frobenius">teorema</a></br>'
        if ranA == ranAb and ranAb == n:
            result += "El rango de A es igual al rango de la matriz aumentada y el rango de A es igual al numero de incognitas, entonces el sistema es compatible determinado y por esto el sistema tiene solucion unica</br>"
        elif ranA == ranAb and ranAb < n:
            result += f"El rango de A es igual al rango de la matriz aumentada pero el rango de la matriz aumentada es menor al numero de incognitas, entonces el sistema es compatible indeterminado y por esto el sistema tiene infinitas soluciones, además el determinante de la matriz es {det:.5f} y por eso el método no converge</br>"
        else:
            result += "El rango de A es menor al rango de la matriz aumentada, entonces el sistema es incompatible y no tiene solucion</br>"
        return A, result
    
A = [[2, -1, 0, 3],[1, 0.5, 3, 8],[0, 13, -2, 11],[14, 5, -2, 3]]

#b = [[1],[1],[1],[1]]

b = [1,1,1,1]

print(eliminacionSimple(A,b))