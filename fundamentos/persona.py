class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad



# creacion de un objeto 
persona = Persona("karla",30)
print(persona.nombre,persona.edad)


#creacion de un segundo objeto 
persona2 = Persona("carlos",40)
print(persona2.edad, persona2.nombre)



