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
            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s' # nos conecta con la tabla persona (%s = placeholder)
            entrada = input('Digite los id_persona a buscar (separados por coma): ')
            llaves_primarias = (tuple(entrada.split(', ')),)#asi se escribe la tupla de tuplas
            cursor.execute(sentencia, llaves_primarias) #ejecutamos la consulta de id_persona en modo tupla
            registros = cursor.fetchall() # obtenemos los registros(techone o techall segun corresponda
            for registro in registros:
                print(registro) #mostramos los registros en forma de tupla
except Exception as e:
    print(e)(f'Ocurrió un error: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html