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
    conexion.autocommit = False #True no es una buena practica, inicia transaccion
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email)VALUES(%s,%s,%s)'
    #podemos modificar el largo de caracteres desde postgreSQL
    valores = ('Jorge','Prol','jprol@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('Juan Carlos','Perez','jjuarez@mail.com', 15)
    cursor.execute(sentencia, valores)

    #se cierra la transaccion
    conexion.commit() #Hacemos commit manualmente con conexion.autocommit = False //con with se hace automaticamente
    print('Termina la transaccion')
except Exception as e:
    conexion.rollback() #con with se hace de manera automatica
    print(f'Ocurrió un error, se hizo un rollback: {e}')
finally:
    conexion.close()

#https://www.psycopg.org/docs/usage.html
