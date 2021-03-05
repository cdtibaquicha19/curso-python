from herencia_multiple.figuras_geometricas import FiguraGeometrica
from herencia_multiple.color import Color
# Creamos la clase hijo
class Cuadrado(FiguraGeometrica,Color):
    #inicializar la clase hijo y las variables a solicitar
    def __init__(self,lado,color):
        #inicializamos las clases padre llamando los atributos solo la clase 
        FiguraGeometrica.__init__(self,lado ,lado)
        Color.__init__(self, color)
        
        #se asigna la funcion en este nivel ya que depende de las clases pdres anteriormente declaradas 
    def area(self):
        return self.alto * self.ancho
 
    

        

        
       
        