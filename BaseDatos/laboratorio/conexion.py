from logger_base import logger
from psycopg2 import pool

import sys

class Conexion:
    __DATABASE= 'test_db'
    __USERNAME= 'postgres'
    __PASSWORD ='admin'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None
    @classmethod
    
    def obtenerPool(cls):
        if cls.__pool is None :
            try:
                cls.__pool = pool.SimpleConnectionPool(
                    cls.__MIN_CON,
                    cls.__MAX_CON,
                    host=cls.__HOST,
                    user=cls.__USERNAME,
                    password = cls.__PASSWORD,
                    port= cls.__DB_PORT,
                    database= cls.__DATABASE
                    )
                logger.debug(f'Creacion pool exitosa : {cls.__pool } ')
                return cls.__pool
                
            except  Exception as e : 
                logger.error(f'ha ocurrido un erro en el pool de conexiones  {e}')
                sys.exit()
        else:
            return cls.__pool
    
    
    @classmethod
    def obtenerConexion(cls):
        
        #obtner una conexion del objeto pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
        
    @classmethod
    
    def liberarConexion(cls,conexion):
        #regresar el objeto conexion al pool 
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'Regresamos la conexion al pool : {conexion}')
        logger.debug(f'Estado del pool : {cls.__pool}')
        
    @classmethod
    
    def cerrarConexiones(cls):
        #cerrar el pool y sus conexiones 
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos todas las conexiones del pool : {cls.__pool} ')
        

if __name__ == '__main__':
    #obtener una conexion apartir del pool 
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    #regresar las conexiones al pool
    
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    
    #Cerramos el pool
    Conexion.cerrarConexiones()
    
    
    
    
       
            
