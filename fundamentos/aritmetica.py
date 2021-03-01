#definicion de clase con atributos 
class Aritmetica :
    def  __init__(self, operando1,operando2):
        self.operando1 = operando1
        self.operando2 = operando2
     # se declara una funcion    
    def sumar(self , operando1,operando2):
        #llamo los valores y los opero luego retorno el valor de la operacion realizada 
       return operando1 + operando2
    def restar(self):
        #llamo los valores y los opero luego retorno el valor de la operacion realizada 
       return self.operando1 - self.operando2 
    def multiplicar(self):
        #llamo los valores y los opero luego retorno el valor de la operacion realizada 
       return self.operando1 * self.operando2 
    def dividir(self):
        #llamo los valores y los opero luego retorno el valor de la operacion realizada 
       return self.operando1 / self.operando2 
   
#creamos un objeto de la clase 

aritmetica = Aritmetica(2,5)
print("RESULTADO DE LA SUMA ", aritmetica.sumar(5,5))
print("RESULTADO DE LA RESTA ", aritmetica.restar())
print("RESULTADO DE LA MULTIPLICAR ", aritmetica.multiplicar())
print("RESULTADO DE LA DIVIDIR ", aritmetica.dividir())






   
        
        
       
        