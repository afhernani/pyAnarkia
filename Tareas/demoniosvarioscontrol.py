'''
Controlar la ejecución de varios demonios:
Cuando un programa utiliza un número indeterminado de demonios y se pretende que el hilo
principal espere a que todos terminen su ejecución, utilizaremos join() con cada demonio. Para
hacer el seguimiento de los hilos activos se puede emplear enumerate() pero teniendo en cuenta
que dentro de la lista que devuelve se incluye el hilo principal. Con este hilo hay que tener
cuidado porque no acepta ciertas operaciones, por ejemplo, no se puede obtener su nombre con
getName() o utilizar el método join().
En el ejemplo se emplea la función threading.main_thread() para identificar al hilo principal.
Después, se recorren todos los hilos activos para ejecutar join(), excluyendo al principal
'''

import threading

def contar(numero):
	contador = 0
	while contador<10:
		contador+=1
		print(numero, threading.get_ident(), contador)

		
def main():
	for numero in range(1, 11):
		hilo = threading.Thread(target=contar, args=(numero,), daemon=True)
		hilo.start()

	# Obtiene hilo principal
	hilo_ppal = threading.main_thread()
	# Recorre hilos activos para controlar estado de su ejecución
	for hilo in threading.enumerate():
		# Si el hilo es hilo_ppal continua al siguiente hilo activo
		if hilo is hilo_ppal:
			continue
		# Se obtiene información hilo actual y núm. hilos activos
		print(hilo.getName(), hilo.ident, hilo.isDaemon(), threading.active_count())
		# El programa esperará a que este hilo finalice:
		hilo.join()
	
if __name__ == '__main__':
	main()