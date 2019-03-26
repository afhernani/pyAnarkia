'''
Acceso concurrente con semáforos:
Un objeto Semaphore es un instrumento de bloqueo avanzado que utiliza un contador interno
para controlar el número de hilos que pueden acceder de forma concurrente a una parte del
código. Si el número de hilos que intentan acceder supera, en un momento dado, al valor
establecido se producirá un bloqueo que será liberado en la medida que los hilos no bloqueados
vayan completando las operaciones previstas.
Realmente actúa como un semáforo en la entrada de un aparcamiento público: dejando pasar
vehículos mientras existen plazas disponibles y cerrando el acceso hasta que no quede libre al
menos una plaza.
Obviamente, este dispositivo se utiliza para restringir el acceso a recursos con capacidad
limitada.
En el siguiente ejemplo se generan cinco hilos para simular una descarga simultánea de
archivos. Las descargas podrán ser concurrentes hasta un máximo de 3 (es el valor que tiene la
constante NUM_DESCARGAS_SIM que se utiliza para declarar el objeto Semaphore).
'''
import threading
import time

def descargando(semaforo):
	global activas
	nombre = threading.current_thread().getName()
	print('Esperando para descargar:', nombre)
	with semaforo:
		activas.append(nombre)
		print('Descargas activas', activas)
		print('...Descargando...', nombre)
		time.sleep(0.1)
		activas.remove(nombre)
		print('Descarga finalizada', nombre)


NUM_DESCARGAS_SIM = 3
activas = []

def main():
	semaforo = threading.Semaphore(NUM_DESCARGAS_SIM)
	for indice in range(1,6):
		hilo = threading.Thread(target=descargando,
								name='D' + str(indice),
								args=(semaforo,),)
		hilo.start()

if __name__ == '__main__':
	main()