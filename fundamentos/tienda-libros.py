
print("Proporcione los siguientes datos del libro ")
nombre = input("Proporciona el nombre ")
i = int(input("proporciona el id del libro "))
precio = float(input("Proporcione precio del libro "))
enviogratuito = input("Indica si el envio es gratuito (True/False) ")

if enviogratuito  == "True" :
    enviogratuito = True 
elif enviogratuito =="False": 
    enviogratuito = False
else:
    enviogratuito ="Valor incorrecto debe ser True/False"  
    
print("Nombre de libro :" , nombre)
print("ID :" , i)  
print("Precio :" , precio)  
print("envio gratuito  :" , enviogratuito)  
# se muestra el vtipo de dato que esta generando la variable 
print (type(nombre))



