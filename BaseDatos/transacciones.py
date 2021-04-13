import psycopg2 
#conexion 
conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1', 
                            port='5432',
                            database='test_db')

try:
    
    cursor = conexion.cursor()
   
    sql = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    valores= ('cmaria','lara','mlara@mail.com')
    registros_insertados=0
    
    cursor.execute(sql,valores)
    registros_insertados +=cursor.rowcount

    sql = 'UPDATE persona SET nombre= %s, apellido= %s, email= %s WHERE id_persona= %s'
    valores= ('carlos1','laran1','claranuevo@mail.com',14 )
    
    cursor.execute(sql,valores)

    #guardamos la informacion que esta pendiente en la base de datos 
    conexion.commit()
    
    #Cuenta cuantos registros fueron insertados 
    registros_insertados +=cursor.rowcount

    print(f'Registros insertados : {registros_insertados}')
    
except Exception as e :
    #da rolback marcha atras a todas las operaciones pendientes 
    conexion.rollback()
    print(
            f"Ocurrio un error en la transaccion : {e}"
        )
finally:
    cursor.close()
    conexion.close()