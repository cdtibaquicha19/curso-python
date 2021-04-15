from persona import Persona
from logger_base import logger
from cursor_del_pool import CursorDelPool

class PersonaDao:
    '''
    DAO (Data Access Object) 
    CRUD: Create-Read-Update-Delete entidad Persona
    '''
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO  persona (nombre,apellido,email) VALUES (%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s , apellido=%s , email=%s WHERE id_persona = %s'
    __ELIMINAR='DELETE FROM persona WHERE id_persona=%s'
    
    
    @classmethod
    def seleccionar(cls):
        
       with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            
            for registro in registros:
                
                persona = Persona(registro[0], registro[1], registro[2], registro[3])
                personas.append(persona)
            
            return personas  
    
    @classmethod
    def insertar(cls, persona):
        
       with CursorDelPool() as cursor:
            
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Persona a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR, valores)

            return cursor.rowcount
        
            
    @classmethod
    def actualizar(cls, persona):
        
       with CursorDelPool() as cursor:
           
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Persona a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(),persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR, valores)
            
            return cursor.rowcount
        
            
    @classmethod
    def eliminar(cls, persona):
        
       with CursorDelPool() as cursor:
           
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Persona a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR, valores)
           
            return cursor.rowcount
            
                  
    
if __name__ == '__main__':
    #ersonas = PersonaDao.seleccionar()    
    #for persona in personas:
    #    logger.debug(persona)
    
    
    #persona = Persona(nombre='cristyan' ,apellido='tibaquicha',email='ctibaquicha2@mail.com')
    #personas_insertadas = PersonaDao.insertar(persona)
    #logger.debug(f'Personas insertadas :{personas_insertadas}')
    
    #persona = Persona(35,'juan' , 'perez' , 'jperez@mail.com'  )
    #personas_editadas = PersonaDao.actualizar(persona)
    #logger.debug(f'Personas actualizadas : {personas_editadas} ')
    
    
    #persona = Persona(id_persona=35)
    #personas_eliminadas = PersonaDao.eliminar(persona)
    #logger.debug(f'Personas eliminadas : {personas_eliminadas} ')
    
    pass
    
    
    