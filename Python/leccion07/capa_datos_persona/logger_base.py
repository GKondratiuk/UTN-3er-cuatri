import logging as log #importamos el login y le ponemos un alias
#las sentencias a continuacion nos iran mostrando los mensajes segun los niveles
#https://docs.python.org/3/howto/logging.html
log.basicConfig(level=log.DEBUG,#llamamos a una configuracion basic
                format ='%(asctime)s:%(levelname)s:[%(filename)s:%(lineno)s] %(message)s',
                datefmt='%I:%M:%S%p ', #ordenamos por horas, minutos y segundos
                handlers=[
                log.FileHandler('capa_datos.log'),
                log.StreamHandler()
                ])
if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel info')
    log.warning('Mensaje a nivel warning')
    log.error('Mensaje a nivel error')
    log.critical('Mensaje a nivel critical')