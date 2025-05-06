class Personaje:
    def __init__(self,nombre,genero):
        self._genero = genero
        self._nombre = nombre

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self,genero):
        self._genero = genero

    @property
    def nombre(self):
        return self._nombre

    @genero.setter
    def nombre(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f"El nombre de tu personaje es {self._nombre} y es {self._genero}"

if __name__ == "__main__":
    personaje1 = Personaje("Matheus","Hombre")
    print(personaje1)
