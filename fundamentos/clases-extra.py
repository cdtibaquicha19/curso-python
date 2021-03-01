class Persona:
    def __init__(this, n, e,*v,**d):
        this.nombre = n
        this.edad = e
        this.valores = v 
        this.diccionario = d
        
    def desplegar(this):
        print("Nombre: ",this.nombre)
        print("Edad: ",this.edad)
        print("Valores (tupla)", this.valores)
        print("Diccionario", this.diccionario)
        

print()
        
p1 = Persona("juan" , 28)
p1.desplegar()
print()
p2 = Persona("karla" ,30 , 2,4,5)
p2.desplegar()
print()

p3 = Persona("paola", 30 , 4,9 , m="manzana" , p= "pera" ,b= "banana")
p3.desplegar()