'''
Hilos con argumentos:
Para ajustar el comportamiento de los programas que usan hilos nada mejor que tener la
posibilidad de pasar valores a los hilos. Para eso están los argumentos args y kwargs en el
constructor.
En el siguiente ejemplo se utilizan estos argumentos para pasar una variable con el número de
hilo que se ejecuta en un momento dado y un diccionario con tres valores que ajustan el
funcionamiento del contador en todos los hilos
'''
import threading

def contar(num_hilo, **datos):
	contador = datos['inicio']
	incremento = datos['incremento']
	limite = datos['limite']
	while contador<=limite:
		print('hilo:', num_hilo, 'contador:', contador)
		contador+=incremento


def main():
	for num_hilo in range(3):
		hilo = threading.Thread(target=contar, args=(num_hilo,),
									kwargs={'inicio':0,
									'incremento':1,
									'limite':10})
		hilo.start()

		
if __name__ == '__main__':
	main()