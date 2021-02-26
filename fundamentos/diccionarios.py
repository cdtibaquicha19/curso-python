#diccionarios esta compuesto de llave y valor (key,value)

diccionario = {
    "IDE" : "Integrated development environment",
    "OPP" : "Object oriented programing",
    "DMS" : "Database management system"
}
print(diccionario)
# funciones 
print(len(diccionario))
#aaceder al elemento de un diccionario 

print(diccionario["IDE"])
#OTRA FORMA DE ACCEDER A LOS ELEMENTOS 
print(diccionario.get("IDE"))

#modificar valores 
diccionario["IDE"]= "Integrate 2 "
print(diccionario.get("IDE"))

#iterar elementos 
for termino in diccionario : 
     print(diccionario[termino])
     
for valor in diccionario.values():
    print(valor)

#comprobar si existe 
print("IDE" in diccionario)

#agregar un elemento 
diccionario["PK"] = "Primary Key "
print(diccionario)

#remover elementos 
diccionario.pop("DMS")
print(diccionario)

#Limpiar el diccionario 
diccionario.clear()
print(diccionario)
#eliminar 
del diccionario




    






