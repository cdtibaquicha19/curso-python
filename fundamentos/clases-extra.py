class Persona:
    def __init__(self, n, e,*v,**d):
        self.nombre = n
        self.edad = e
        self.valores = v 
        self.diccionario = d
        
    def desplegar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Valores (tupla)", self.valores)
        print("Diccionario", self.diccionario)
        

print()
        
p1 = Persona("juan" , 28)
p1.desplegar()
print()
p2 = Persona("karla" ,30 , 2,4,5)
p2.desplegar()
print()

p3 = Persona("paola", 30 , 4,9 , m="manzana" , p= "pera" ,b= "banana")
p3.desplegar()