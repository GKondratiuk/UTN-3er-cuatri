import psycopg2 as bd # Esto es para conectarnos a postgre "pip install psycopg2-binary" en linux o sin el "-binary" en windows

conexion = bd.connect( #conectamos a la base de datos
    user = 'guille',
    password = '0088',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
)
#print(conexion) probamos si hay conexion
try:
    with conexion: #agregamos la conexion
        with conexion.cursor() as cursor: # conexion del cursor
            sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)'
            valores = ('Alex','Rojas','arojas@mail.com')
            cursor.execute(sentencia, valores)

            sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
            valores = ('Juan Carlos','Roldan','jcroldan@mail.com', 15)
            cursor.execute(sentencia, valores)

except Exception as e:
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()

print('Termina la transaccion')
#https://www.psycopg.org/docs/usage.html