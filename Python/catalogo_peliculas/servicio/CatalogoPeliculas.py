import os

class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt' #creamos un archivo de texto de peliculas

    @classmethod #creamos un metodo
    def agregar_peliculas(cls,pelicula): #cls es contexto de clase
        with open(cls.ruta_archivo,'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo,'r', encoding='utf8') as archivo:
            print(f'Catalogo de peliculas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_pelicula(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo elminado: {cls.ruta_archivo}')







