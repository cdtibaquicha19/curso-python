class MiClase:
    
    variable_clase = "variable clase"
    
    def __init__(self):
        self.variable_instacia = "variable instancia "
        
        
    @staticmethod
    def metodo_estatico():
        print("metodo estatico")
        print(MiClase.variable_clase)
        # desde un metodo estatico no se puede acceder a una variable de instancia 
        #print(MiClase.variable_instacia)

    @classmethod
    def metodo_clase(cls):
        print("metodo de clase "+ str(cls))
        print(cls.variable_clase)
    # desde un metodo estatico no se puede acceder a una variable de instancia 
        #print(cls.variable_instacia)
    
    def metodo_instancia(self):
        self.metodo_estatico()
        self.metodo_clase()
         
MiClase.metodo_estatico()
MiClase.metodo_clase()


print()
objeto1 = MiClase()
objeto1.metodo_instancia()




        
        