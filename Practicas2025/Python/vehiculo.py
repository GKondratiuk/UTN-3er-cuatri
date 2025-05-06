#puede contener importaciones
#clase y nombre de la clase
class Vehiculo:
    def __init__(self,tipo,marca): # metodo y parametros - estan encapsulados, significa que ocultan detalles y protegen datos
        self._marca = marca # atributo protegido "_" y valor
        self._tipo = tipo # atributo protegido "_" y valor

    @property #indica solo lectura
    def marca(self): #metodo get
        return self._marca #devuelve la marca
    @marca.setter #indicador de setter
    def marca(self,marca):#definimos metodo seter
        self._marca = marca #atributo que modifica el valor

    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,tipo):
        self._tipo = tipo

    def __str__(self): # metodo para generar una cadena para mostrar la informacion
        return f"Tu vehiculo es un/a {self._tipo} de marca {self._marca}"

if __name__ == "__main__":
    vehiculo1 = Vehiculo("Moto","Suzuki")
    print(vehiculo1)

