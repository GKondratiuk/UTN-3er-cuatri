import psycopg2 # Esto es para conectarnos a postgre "pip install psycopg2-binary" en linux o sin el "-binary" en windows

conexion = psycopg2.connect( #conectamos a la base de datos
    user = 'guille',
    password = '0088',
    host = '127.0.0.1',
    port = '5432',
    database = 'test_bd'
)
#print(conexion) probamos si hay conexion

cursor = conexion.cursor() #objeto que permite ejecutar sentencias
sentencia = 'SELECT * FROM producto' # nos conecta con la tabla persona
cursor.execute(sentencia) #ejecutamos la consulta
registros = cursor.fetchall() # obtenemos los registros
print(registros) #mostramos los registros en forma de tupla

cursor.close()
conexion.close()