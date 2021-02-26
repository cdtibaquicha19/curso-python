#coleccion sin orden , no tienen un orden o indice , no tienen elementos repetidos 
#los elementos no se pueden modificar , pero si agregar nuevos y modificar 

planetas = {"marte","jupiter","venus"}
print(planetas)

#metodos
#revisar largo 
print(len(planetas))

#revisar si un elemento esta dentro 
print("marte" in planetas)

# no se pueden mofificar pero si eliminar el objeto 
planetas.add("tierra")
print(planetas)
#eliminar 
planetas.remove("tierra")
print(planetas)
# eliminar con discard no arroja error
planetas.discard("jupiter")
print(planetas)
#limpiar el set 
planetas.clear()
print(planetas)
#eliminar la varibale 
del planetas


