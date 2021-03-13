class Persona:
    def __init__(self, nombre):
        self.__nombre = nombre
     
    #metodo sobrescrito de la clase object     
    def __add__(self ,otro):
        return self.__nombre +" "+ otro.__nombre
    
    def __sub__(self, otro):
        return "operacion no soportada"

p1 = Persona("Cristyan")
p2 = Persona("Karla")

print(p1 + p2)
print(p1 - p2)


