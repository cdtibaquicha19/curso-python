import psycopg2 
#conexion 
conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1', 
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()

#consulta sql 
sql = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
#creamos la carga de valores 
valores= ('carlos','lara','clara@mail.com')

cursor.execute(sql,valores)
#guardamos la informacion que esta pendiente en la base de datos 
conexion.commit()

#Cuenta cuantos registros fueron insertados 
registros_insertados = cursor.rowcount

print(f'Registros insertados : {registros_insertados}')




cursor.close()
conexion.close()
