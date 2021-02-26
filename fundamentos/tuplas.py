# tupla mantiene el orden pero no se puede modificar 

frutas = ("naranja" , "platano" , "guayaba") 
print(frutas)
# largo 
print(len(frutas))
# acceder a un elemento 
print(frutas[0])
# navegacion inversa 
print(frutas[-1])
#rango
print(frutas[0:2])
#cambiar indices 
frutaslista = list(frutas)
frutaslista[1] ="platanito"# se debe convertir a lista ya uqeno lo permite directamente 
frutas = tuple(frutaslista)
print(frutas)
#iterar tupla 
for fruta in frutas:
    print(fruta,end=" ") 
# no se puede agregar ni eliminar elementos de una tupla 
del frutas





