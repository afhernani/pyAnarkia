'''
La situación se hace algo más compleja si se quieren pasar valores utilizando los argumentos
args y/o kwargs porque es necesario reescribir el método __init__(). Por defecto, el constructor
Thread utiliza variables privadas para estos argumentos. En el siguiente ejemplo se declara una
subclase con dos argumentos
'''
import threading

class MiHilo(threading.Thread):
	def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, *, daemon=None):
		super().__init__(group=group, target=target, name=name, daemon=daemon)
		self.arg1 = args[0]
		self.arg2 = args[1]
		
	def run(self):
		contador = 1
		while contador <= 10:
			print('ejecutando...', 'contador', contador, 'argumento1', self.arg1, 'argumento2', self.arg2)
			contador+=1

def main():
	for numero in range(10):
		hilo = MiHilo(args=(numero,numero*numero), daemon=False)
		hilo.start()

	
if __name__ == '__main__':
	main()