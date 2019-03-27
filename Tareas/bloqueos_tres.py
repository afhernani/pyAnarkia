'''
Bloqueos:
Los objetos RLock son parecidos a los objetos Lock con la diferencia de que permiten que un
bloqueo pueda ser adquirido por el mismo hilo varias veces.
Para concluir este apartado, hacer mención al uso de la declaración with que evita tener que
adquirir y liberar explícitamente cada bloqueo. En el ejemplo siguiente las dos funciones que
llaman los hilos son equivalentes:
'''

import threading


def con_with(bloqueo):
    with bloqueo:
        print('Bloqueo adquirido con with')
        print('Procesando...')


def sin_with(bloqueo):
    bloqueo.acquire()
    try:
        print('Bloqueo adquirido directamente')
        print('procesando...')
    finally:
        bloqueo.release()


def main():
    bloqueo = threading.Lock()
    hilo1 = threading.Thread(target=con_with, args=(bloqueo,))
    hilo2 = threading.Thread(target=sin_with, args=(bloqueo,))


if __name__ == '__main__':
    main()
