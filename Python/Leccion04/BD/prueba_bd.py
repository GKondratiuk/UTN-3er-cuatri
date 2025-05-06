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
            sentencia = 'SELECT * FROM persona WHERE id_persona =  %s' # nos conecta con la tabla persona (%s = placeholder)
            id_persona = input('Digite un número para el id_persona: ')
            cursor.execute(sentencia,(id_persona,)) #ejecutamos la consulta de id_persona en modo tupla
            registros = cursor.fetchone() # obtenemos los registros(techone o techall segun corresponda
            print(registros) #mostramos los registros en forma de tupla
except Exception as e:
    print(e)(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html