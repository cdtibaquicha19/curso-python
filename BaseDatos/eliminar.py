import psycopg2 
#conexion 
conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1', 
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()

#consulta sql 
sql = 'DELETE FROM  persona  WHERE id_persona= %s'
#creamos la carga de valores 
entrada = input("ingresa el valor a eliminar : ")
valores= (entrada,)
cursor.execute(sql,valores)
#guardamos la informacion que esta pendiente en la base de datos 
conexion.commit()

#Cuenta cuantos registros fueron insertados 
registros_eliminados = cursor.rowcount

print(f'Registros eliminados: {registros_eliminados}')

cursor.close()
conexion.close()
