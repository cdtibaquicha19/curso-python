class Persona :
    #definicion de atributos del objeto como privados 
    def __init__(self):
        self.__nombre = None
        self.__edad = None
    # se crean lo metodos de entrada y salida de datos get y set 
    def get_nombre(self):
        return self.__nombre 
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad = edad 

# se crea el objeto de la clase persona 
p1 = Persona()
# se ingresan los valores por el metodo set 
p1.set_nombre("cristyan")
p1.set_edad(26)
# se imprimen y se leen los atributos con el metodo get 
print("nobre : ",p1.get_nombre() ," y su edad es : ", p1.get_edad())