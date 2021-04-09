import psycopg2 
#conexion 
conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1', 
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()

#consulta sql 
sql = 'UPDATE persona SET nombre= %s, apellido= %s, email= %s WHERE id_persona= %s'
#creamos la carga de valores 
valores= ('carlosnuevo','laranuevo','claranuevo@mail.com', 1)

cursor.execute(sql,valores)
#guardamos la informacion que esta pendiente en la base de datos 
conexion.commit()

#Cuenta cuantos registros fueron insertados 
registros_actualizados = cursor.rowcount

print(f'Registros actualizados: {registros_actualizados}')




cursor.close()
conexion.close()
