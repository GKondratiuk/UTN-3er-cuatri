from logger_base import log
class Persona:
    def __init__(self,id_persona=None,nombre=None,apellido=None,email=None): #metodo dunder init
        #None para que el dato sea opcional
        self.id_persona = id_persona
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):#metodo dunder str
        return f'''
            Id Persona: {self.id_persona}, 
            Nombre: {self.nombre}, 
            Apellido: {self.apellido}, 
            Email: {self.email}
'''
#METODOS GETTERS AND SETTERS
@property
def id_persona(self):
    return self._id_persona

@id_persona.setter
def id_persona(self,id_persona):
    self._id_persona = id_persona

@property
def nombre(self):
    return self._nombre

@nombre.setter
def nombre(self,nombre):
    self._nombre = nombre

@property
def apellido(self):
    return self._apellido

@apellido.setter
def apellido(self,apellido):
    self._apellido = apellido

@property
def email(self):
    return self._email

@email.setter
def email(self,email):
    self._email = email

if __name__ == '__main__': #punto de entrada, ejecuta codigo
    persona1 = Persona(88,'Willy','Box','wbox@mail.com')
    log.debug(persona1)
    persona2 = Persona(nombre='Carlitos',apellido='Slash',email='cslash@mail.com')
    #especificamos para evitar el cruce de informacion
    log.debug(persona2)
    persona3 = Persona(id_persona = 1)
    log.debug(persona3)




