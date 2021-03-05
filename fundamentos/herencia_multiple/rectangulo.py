from figuras_geometricas import FiguraGeometrica
from color import Color
# Creamos la clase hijo

class Rectangulo(FiguraGeometrica,Color):
    #inicializar la clase hijo y las variables a solicitar
    def __init__(self,ancho,largo,color):
        #inicializamos las clases padre llamando los atributos solo la clase 
        FiguraGeometrica.__init__(self,ancho ,largo)
        Color.__init__(self, color)
        
        #se asigna la funcion en este nivel ya que depende de las clases pdres anteriormente declaradas 
    def area(self):
        return "el area del rectangulo es "+ str(self.get_alto() * self.get_ancho())
    
    def __str__(self):
        return "los lados son alto :" + str(self.get_alto()) + " ancho " +str(self.get_alto())+" y su color es :" + self.get_color()
 
    

        

        
       
        