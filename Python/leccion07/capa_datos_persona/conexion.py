import psycopg2 as bd

from Leccion04.BD.transacciones import conexion
from logger_base import log
import sys
class Conexion:
    _DATABASE = 'test_bd' #conexion con nuestra bd.postgres
    _USERNAME = 'guille'
    _PASSWORD = '0088'
    _HOST = 'localhost'
    _PORT = '5432'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None: # si no existe conexion
            try: #intentar conectar
                cls._conexion = bd.connect(host=cls._HOST,
                                           user=cls._USERNAME,
                                           password=cls._PASSWORD,
                                           port=cls._PORT,
                                           database=cls._DATABASE)
                log.debug(f'Conexion exitosa: {cls._conexion}')
                return cls._conexion # retornar conexion

            except Exception as e: #si no se conecta...
                log.error(f'Error conexion: {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'Conexion exitosa, se abrió correctamente el cursor: {cls._cursor}')
                return cls._cursor

            except Exception as e:
                log.error(f'Ocurrió un Error de conexion: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__ == '__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()