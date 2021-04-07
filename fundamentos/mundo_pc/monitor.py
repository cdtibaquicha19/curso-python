class Monitor:
    contador_monitores = 0 
    
    def __init__(self, marca , tamanio):
        Monitor.contador_monitores += 1 
        self.__id_monitores =  Monitor.contador_monitores
        self.__marca =  marca
        self.__tamanio = tamanio
        
    def get_id_monitores(self):
        return self.__id_monitores
    
    def set_id_monitores(self, id_monitores):
        self.__id_monitores = id_monitores
    
    def get_marca(self):
        return self.__marca
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def get_tamanio(self):
        return self.__tamanio
    
    def set_tamanio(self, tamanio):
        self.__tamanio = tamanio
        
    def __str__(self):
        return (
            f"Id : {self.__id_monitores} "
            f"Marca : {self.__marca}, "
            f"Tamaño: {self.__tamanio} " 
        )
    

