condicion = True
if condicion == True:
    print("La condicion es verdadera ")
elif condicion == False:
    print("Condicion falsa")
else:
    print("Condicion no reconocida")
# SEGUNDO METODO SIMPLIFICADO DEL ELSE IF 
print("condicion verdadera ") if condicion else print ("condicion falsa")
 # EJERCICIO 
numero = int(input("Proporciona un numero entre 1 y 3 "))
if numero == 1 :
    numerotexto ="Numero 1 "
elif numero == 2 :
    numerotexto = "Numero 2" 
elif numero == 3 :
    numerotexto = "Numero 3 " 
else:
    numerotexto ="Valor fuera de rango "
print("Numero proporcionado" , numerotexto)