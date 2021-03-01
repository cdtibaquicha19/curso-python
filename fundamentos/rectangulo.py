class Rectangulo:
    def __init__(self,base,altura):
        self.base = base 
        self.altura = altura 
    def calcular_area(self):
        return self.base*self.altura 
    
base = int(input("Proporciona la Base :")) 
altura = int(input("Proporciona laAltura :"))  
 
rectangulo  = Rectangulo(base,altura)

print ("El area del rectangulo es : ",rectangulo.calcular_area() )  
 


