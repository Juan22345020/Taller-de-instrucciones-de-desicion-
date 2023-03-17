
print("-----------------------------")
print("---------EJERCICIO 2---------")
print("-----------------------------")

Ingresos = int(input("DIGITE SUS INGRESOS: "))
Deudas = int(input("DIGITE 0 si no tiene deudas, digite 1 si las tiene: "))

if (Ingresos>945200):
    if(Deudas==1):
        print("NO APROBADO")
    else:
        if(Deudas==0):
         print("APROBADO")
        else:
           print("NO APROBADO") 
else:
    print("NO APROBADO")

print("-----------------------------")
print("---------RESULTADOS----------")
print("-----------------------------")