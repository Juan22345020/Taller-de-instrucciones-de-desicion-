print("--------------------------------")
print("------------EJERCICIO 1---------")
print("--------------------------------")


X = int(input("Digite el valor de X: "))
Y = int(input("Digite el valor de Y: "))

if (X==Y):
    if (Y==0):
        print("La coordenada esta ubicada en el punto de origen")
    else:
        print("La coordenada esta ubicada en el EJE Y")
else:
    if(Y==0):
         print("La coordenada esta ubicada en el eje x")
    else:
         if(X>0):
            if(X>0):
             print("La coordenada esta ubicada en el Cuadrante I")
            else:
             print("La coordenada esta ubicada en el Cuadrante IV")
         else:
           if(Y>0):
            print("La coordenada esta ubicada en el Cuadrante II")
           else:
            print("La coordenada esta ubicada en el Cuadrante III")

print("-------------------------------")
print("--------RESULTADOS-------------")
print("-------------------------------")
