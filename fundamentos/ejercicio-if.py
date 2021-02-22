#ejercicio para valir la estacion de cada mes ingresado por usuario 
mes  = int(input("proporciona el mes del año entre : 1 a 12 "))
estacion = None
if ((mes==1) or (mes == 2)or (mes==3)):
    estacion = "Invierno"
elif ((mes==4) or (mes == 5)or (mes==6)):
    estacion = "Otoño"
elif ((mes==7) or (mes == 8)or (mes==9)):
    estacion = "Verano"
elif ((mes==10) or (mes == 11)or (mes==12)):
    estacion = "primavera"
else:
    print("Valor fuera de rango " , mes)
print("la estacion es " , estacion)
    
    
    
    