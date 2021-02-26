nombres = ["juan","karla","ricardo" , "maria"]
print(nombres)
# conocer el largo de la lista 
print(len(nombres))
#elemento 0 
print(nombres[0])
# navegar a la inversa 
print(nombres[-1])
# recuperar rango 
print(nombres[0:2])#sin incluir el indice 2 
#imprimir los elementos de inicio hasta le indice proporcionado 
print(nombres[:3])
#imprimir elementos hasta el final del inidice proporcionado 
print(nombres[1:])
#comabiar elementos de una lista 
nombres[3] ="ivone "
print(nombres)
#iterar  la lista 
for nombre in nombres:
    print(nombre)
#revisar si existen un elemento en la lista 
if "karla" in nombres:
    print("si existe el nombre karla ")
else:
    print("el elmento buscado no existe en la lista ")

#agregar un nuevo elemento a la lista 
nombres.append("lorenzo")
print(nombres)
#insertar en indice asignado 
nombres.insert(1,"octavio")
print(nombres)
#eliminar un elemento de la lista 
nombres.remove(nombres[1])
print(nombres)
#elimina el ultimo elemento de la lista 
nombres.pop()
#eliminar el indicado 
del nombres[0]
print(nombres)
#limpirar elementos de la lista 
nombres.clear()
print(nombres)
del nombres 










     


