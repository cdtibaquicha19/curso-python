import psycopg2 

conexion = psycopg2.connect(user='postgres',
                            password='admin', 
                            host='127.0.0.1', 
                            port='5432',
                            database='test_db')

cursor = conexion.cursor()
sql = 'SELECT * FROM  persona WHERE id_persona= %s'
id_persona = int(input("Proporciona la llave primaria a buscar: "))
llave_primaria= (id_persona,)
cursor.execute(sql,llave_primaria)
registros = cursor.fetchone()
print(registros)

cursor.close()
conexion.close()

