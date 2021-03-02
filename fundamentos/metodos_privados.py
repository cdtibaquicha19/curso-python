class Persona :
     def __init__(self,nombre,ape_paterno,ape_materno):
         self.nombre = nombre
         self._ape_paterno = ape_paterno
         self.__ape_materno = ape_materno
         
     def metodo_publico(self):
         self.__metodo_privado()   
         
     def __metodo_privado(self):
        print(self.nombre)
        print(self._ape_paterno) 
        print(self.__ape_materno)
        
     def get_ape_materno(self):
         return self.__ape_materno ;
     
     def set_ape_materno(self,ape_materno):
         self.__ape_materno = ape_materno 
                      
p1 = Persona("juan","lopez","perez")   
p1.metodo_publico()
      
         
        