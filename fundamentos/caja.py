class Caja:
    def __init__(self, largo , ancho , alto ):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    def calcular_volumen(self):
        return self.ancho* self.largo * self.alto
    
alto = int(input("alto : "))
ancho = int(input("ancho : "))
largo = int(input("largo : "))

caja = Caja(largo,ancho,alto)

print("el radio de la caja es de :", caja.calcular_volumen())
    