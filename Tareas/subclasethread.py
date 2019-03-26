'''
Creando una subclase Thread y redefinir sus metodos.
Cuando comienza la ejecución de un hilo se invoca, automáticamente, al método subyacente
run() que es el que llama a la función pasada al constructor. Para crear una subclase Thread es
necesario reescribir como mínimo el método run() con la nueva funcionalidad
'''
import threading

class MiHilo(threading.Thread):
	def run(self):
		contador = 1
		while contador <= 10:
			print('ejecutando',
				threading.current_thread().getName(),
				contador)
			contador+=1
	

def main():
	for numero in range(10):
		hilo = MiHilo()
		hilo.start()
	
if __name__ == '__main__':
	main()