
from logger_base import logger

class Persona:
    def __init__(self , id_persona=None , nombre=None ,apellido =None , email=None):
        self.__id_persona = id_persona
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__email = email
    
    
    def __str__(self):
        return (
                f'Id Persona : {self.__id_persona} ,'
                f'Nombre : {self.__nombre}, '
                f'Apellido : {self.__apellido}, '
                f'Email : {self.__email} '
            )
    
#agregar metodos ge y set  de los atributos 

    def get_id_persona(self):
        return self.__id_persona
    def set_id_persona(self, id_persona):
        self.__id_persona = id_persona
        
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self, apellido):
        self.__apellido = apellido
    
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    

if __name__ =='__main__':
    perosna1 = Persona(1,'Juan', 'Perez','jperez@mail.com')
    logger.debug(perosna1)
    #simulando un objeto a insertar 
    persona2 = Persona(
        nombre= 'carla' ,
        apellido='gomez' ,
        email= 'cgomez@mail.com'
        )
    logger.debug(persona2)
    #simular el caso de eliminar un objeto de tipo persona 
    
    persona3 = Persona(id_persona=3)
    logger.debug(persona3)