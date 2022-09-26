T = float(input("Ingrese su tolerancia : "))

if T <= 0:

  print("Debe ingresar una tolerancia válida")

else:

  I = int(input("Ingrese su numero de Iteracciones deseados : "))

  if I < 0 :

    print("Debe ingresar un numero de iteracciones validos : ")

  else:

    expre = input("Ingrese su funcion sin omitir los signos aritmeticos, en función a X : ")

    x = int(input("Ingrese el valor de prueba : "))

    y = eval(expre)

    fX1 = "y={}".format(y)

    V1 = y

    print("f(",x,") es igual a ", V1)

    X1 = x

    expre2 = input("Ingrese la derivada de la funcion sin omitir los signos aritmeticos, en función a X : ")

    y = eval(expre2)

    fX2 = "y={}".format(y)

    VV = y

    print("f'(",x,") es igual a ", VV)

    XX = x

    expre3 = input("Ingrese la segunda derivada de la funcion sin omitir los signos aritmeticos, en función a X : ")

    x = x

    y = eval(expre3)

    fX3 = "y={}".format(y)

    VVV = y

    print("f''(",x,") es igual a ", VVV)

    XXX = x

    if  V1 != 0:

      x = x

      y = eval(expre)

      fX2 = "y={}".format(y)

      V2 = y

      print("f(",x,") es igual a ", V2)

      X2 = x

      Error = T + 1

      Ini = 0

      while V1 != 0 and Error < T and VV != 0 and VVV != 0 and Ini < I:

        Xini = X1-((V1*VV)/(((VVV)*(VVV))-(V1*VV)))

        Error = Xini - X1

        if Error < 0:

          Error = Error*(-1)

        else:

          Error = Error

        X1 = Xini

        x = X1

        y = eval(expre)

        R1 = "y={}".format(y)

        V1 = y

 

        x = X1

        y = eval(expre2)

        R2 = "y={}".format(y)

        VV = y

        x = X1

        y = eval(expre3)

        R3 = "y={}".format(y)

        VVV = y

 

        Ini = Ini + 1

 

      if Error < T:

        print(X1 , " es una raiz")

      else:

        if VV != 0:

          if VVV != 0:

            print("Limite de iteracione s alcanzado")

          else:

            print("No concluye...")

        else: 

          print(X1," es una raíz")

    else:

      print("Ahi esta la raíz")
