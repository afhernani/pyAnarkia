'''
Demonios:
Existen dos modos diferentes de finalizar un programa basado en hilos. En el primer modo el hilo
principal del programa espera a que todos los hilos creados con Thread terminan su trabajo. Ese
es el caso de todos los ejemplos mostrados hasta ahora.
En el segundo modo, el hilo principal del programa puede finalizar aunque uno o más hilos hijos
no hayan terminado su tarea; teniendo en cuenta que cuando finalice el hilo principal también lo
harán estos hilos especiales llamados demonios. Si existen hilos no-demonios el hilo principal
esperará a que estos concluyan su trabajo. Los demonios son útiles para programas que
realizan operaciones de monitorización o de chequeo de recursos, servicios, aplicaciones, etc.
Para declarar un hilo como demonio se asigna True al argumento daemon al crear el objeto
Thread, o bien, se establece dicho valor con posterioridad con el método set_daemon().
El ejemplo que sigue utiliza dos hilos: un hilo escribe en un archivo y el otro hilo (el demonio)
chequea el tamaño del archivo cada cierto tiempo. Cuando el hilo encargado de escribir termina,
todo el programa llega a su fin a pesar de que el contador del demonio no ha alcanzado el valor
límite
'''

import time, os, threading


def chequear(nombre):
	'''Chequea tamaño de archivo'''
	contador = 0
	tam = 0
	while contador<100:
		contador+=1
		if os.path.exists(nombre):
			estado = os.stat(nombre)
			tam = estado.st_size
		print(threading.current_thread().getName(),
										contador,
										tam,
										'bytes')
		time.sleep(0.1)


def escribir(nombre):
	'''Escribe en archivo'''
	contador = 1
	while contador<=10:
		with open(nombre, 'a') as archivo:
			archivo.write('1')
			print(threading.current_thread().getName(), contador)
			time.sleep(0.3)
			contador+=1

			
def main():
	nombre = 'archivo.txt'
	if os.path.exists(nombre):
		os.remove(nombre)
	hilo1 = threading.Thread(name='chequear',
							target=chequear,
							args=(nombre,),
							daemon=True)
	hilo2 = threading.Thread(name='escribir',
							target=escribir,
							args=(nombre,))
	hilo1.start()
	hilo2.start()

if __name__ == '__main__':
	main()