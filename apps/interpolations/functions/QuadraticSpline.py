import sympy
#import totalPivoting
x = sympy.Symbol('x')
import json

xn = "-1, 0, 3, 4"
fxn = "15.5, 3, 8, 1"


functions = []
result = []
des = []

def convert_string_to_list(string):
    """
        Receive a comma-separated string and convert it to its type
        exm:
            convert_string_to_list("1,2.3,4,5.6")
        result:
            [1,2.3,4,5.6]
            int,float,int,float
    """
    res = f"[{string}]".strip(" ")
    res_to_json = json.loads(res)
    return res_to_json

def createInequality(xn, fxn):
    inequality = []
    for i in range(0, len(xn)-1):
        if (i < len(xn)):
            inequality.append(((xn[i], fxn[i]), (xn[i+1], fxn[i+1])))
    return inequality


def quadratic(xi_str, yi_str ):
    xn = convert_string_to_list(xi_str)
    fxn = convert_string_to_list(yi_str)
    
    n = len(xn)
    ny=len(fxn)
    if(n==ny):
        inequality = createInequality(xn, fxn)
        superMatrix = [[0 for x in range(3*len(inequality)+1)]
                    for y in range(3*len(inequality))]
        n = len(superMatrix)
        j = 0
        z = 0
        result = []
        for i in inequality:
            auxj = str(z-j)
            superMatrix[j][z] = i[0][0]**2
            superMatrix[j][z+1] = i[0][0]
            superMatrix[j][z+2] = 1
            superMatrix[j][n] = i[0][1]
            superMatrix[j+1][z] = i[1][0]**2
            superMatrix[j+1][z+1] = i[1][0]
            superMatrix[j+1][z+2] = 1
            superMatrix[j+1][n] = i[1][1]
            z += 3
            j += 2
        k = j
        z = 0
        for i in range(0, len(inequality)-1):
            superMatrix[k][z] = 2*inequality[i][1][0]
            superMatrix[k][z+1] = 1
            superMatrix[k][z+3] = -2*inequality[i+1][0][0]
            superMatrix[k][z+4] = -1
            superMatrix[k][n] = 0
            k += 1
            z += 3
        superMatrix[k][0] = 1
        # totalPivoting.a = superMatrix
        # totalPivoting.n = len(superMatrix)
        # totalPivoting.marcas = [i for i in range(0, totalPivoting.n)]
        # aux = totalPivoting.elimination()
        # j = 0
        # for i in range(0, len(inequality)):
        #     func = aux[j]*x**2+aux[j+1]*x + aux[j+2]
        #     result.append(f"{inequality[i][0][0]} <= x <= {inequality[i][1][0]} | {func}")
        #     j += 3
            
        return result
    else:
        return("the size of the vectors are different")

#print(quadratic(xn, fxn))

# for i in quadratic():
#     print(i)
