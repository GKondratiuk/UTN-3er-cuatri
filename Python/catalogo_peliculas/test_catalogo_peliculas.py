from Python.catalogo_peliculas.dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas as cp
opcion = None
while opcion != 4:
    try:
        print('opciones: ')
        print('1. Agregar Pelicula')
        print('2. Listar Peliculas')
        print('3. Eliminar catálogo de peliculas')
        print('4. Salir.')
        opcion = int(input('Ingrese la opcion: '))
        if opcion == 1:
            nombre_pelicula = input('Ingrese el nombre del pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_peliculas(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_pelicula()

    except Exception as e:
        print(f'Ocurrió un erro de tipo: {e}')
        opcion = None
    else:
        print('Salimos del programa')