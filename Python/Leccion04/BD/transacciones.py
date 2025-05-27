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
    conexion.autocommit = False #True no es una buena practica
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)'
    valores = ('Maria','Esparza','mesparza@mail.com')
    cursor.execute(sentencia, valores)
    conexion.commit() #Hacemos commit manualmente con conexion.autocommit = False //con with se hace automaticamente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback() #con with se hace de manera automatica
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html
