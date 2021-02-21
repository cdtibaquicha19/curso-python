a =  int(input("ingrese valor a probar en el rango de 1 a 5 "))
valormin =0 
valormax = 5 
dentrorango = (a >= valormin and a<=valormax)
if(dentrorango):
    print("Dentro de rango")
else:
    print("Fuera de rango")

# EJEMPLO CON EXPRESION OR 
 
vacaciones = False
diadescanso = False
if(vacaciones or diadescanso):
    print("puedes ir al partque ")
else:
    print("tienes deberes que hacer ")

#ejemplo de NOT 

print(not(vacaciones))



