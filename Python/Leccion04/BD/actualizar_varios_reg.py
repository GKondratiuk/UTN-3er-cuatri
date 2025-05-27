import psycopg2 # Esto es para conectarnos a postgre "pip install psycopg2-binary" en linux o sin el "-binary" en windows

conexion = psycopg2.connect( #conectamos a la base de datos
    user = 'guille',
    password = '0088',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
)
#print(conexion) probamos si hay conexion
try:
    with conexion:
        with conexion.cursor() as cursor: #objeto que permite ejecutar sentencias
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Jorge Carlos', 'Roldan', 'rcarlos@mail.com', 1),
                       ('Romina', 'Ayala', 'ayalar@mail.com', 5)
            )#tupla de tuplas
            cursor.executemany(sentencia, valores) #ejecutamos la consulta de id_persona en modo tupla
            registros_actualizados = cursor.rowcount #selecciona la cantidad de filas afectadas
            print(f'Los registros insertados son: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html