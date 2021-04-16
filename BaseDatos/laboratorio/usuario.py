
from logger_base import logger

class Usuario:
    def __init__(self , id_usuario=None , username=None ,password =None ):
        self.__id_usuario = id_usuario
        self.__username = username
        self.__password = password
   
    
    
    def __str__(self):
        return (
                f'Id usuario : {self.__id_usuario} ,'
                f'Username : {self.__username}, '
                f'Password : {self.__password} '
            )
    
#agregar metodos ge y set  de los atributos 

    def get_id_usuario(self):
        return self.__id_usuario
    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario
        
    def get_username(self):
        return self.__username
    def set_nombre(self, username):
        self.__username = username
        
    def get_password(self):
        return self.__password
    def set_apellido(self, password):
        self.__password = password


    

if __name__ =='__main__':
    usuario1 = Usuario(1,'Juan' ,'12345')
    logger.debug(usuario1.get_id_usuario())
    
    