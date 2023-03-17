
print("--------------------------------------")
print("-------------EJERCICIO 3--------------")
print("--------------------------------------")



precio = int(input("Digite el precio costo: "))
p = precio * 0.15
x = precio+ 500
y = precio * 0.25

t= p+precio
r= y+precio

if (precio>0 and precio<3000):
    print ("La ganancia sera de: " + str(t))
else:
    if (precio>=3000 and precio<6000):
        print ("El precio costo del objeto es: " + str(x))
    else:
        if (precio>6000):
            print ("La ganancia sera de: " + str(r))
        



print("--------------------------------------")
print("--------------RESULTADOS--------------")
print("--------------------------------------")



