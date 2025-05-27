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
            sentencia = 'INSERT INTO persona (nombre, apellido, email)VALUES(%s, %s, %s)'
            valores = ('Carlos','Lara','clara@mail.com')#es una tupla
            cursor.execute(sentencia, valores) #ejecutamos la consulta de id_persona en modo tupla
            #conexion.commit() guarda los cambios - pero el "with" lo hace de manera automatica
            registros_insertados = cursor.rowcount #selecciona la cantidad de filas afectadas
            print(f'Los registros insertados son: {registros_insertados}')
except Exception as e:
    print(e)(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html