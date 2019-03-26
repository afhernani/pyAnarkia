'''
Sincronizar hilos con objetos Event:
A veces, es necesario que varios hilos se puedan comunicar entre si para sincronizar sus
trabajos. Uno de los mecanismos disponibles se basa en los objetos Event por su capacidad de
anunciar a uno o más hilos (que esperan) que se ha producido un suceso para que puedan
proseguir su ejecución. Para ello, utiliza el valor de una propiedad que es visible por todos los
hilos. Los valores posibles de esta propiedad son True o False y pueden ser asignados con los
métodos set() y clear(), respectivamente.
Por otro lado, el método wait() se emplea para detener la ejecución de uno o más hilos hasta que
la propiedad alcance el valor True. Dicho método devuelve el valor que tenga la propiedad y
cuenta con un argumento opcional para fijar un tiempo de espera. Otra opción para obtener el
estado de un evento es mediante el método is_set().
En el ejemplo siguiente se inician dos hilos que permanecen a la espera hasta la obtención de 25
números pares (los números son generados con la función randint() del módulo random).
Cuando se tienen todos los números los dos hilos continúan su ejecución de manera
sincronizada.
'''

import threading, random

def gen_pares():
	num_pares = 0
	print('Números:', end=' ')
	while num_pares < 25:
		numero = random.randint(1, 10)
		resto = numero % 2
		if resto == 0:
			num_pares +=1
			print(numero, end=' ')
	print()

def contar():
	contar = 0
	nom_hilo = threading.current_thread().getName()
	print(nom_hilo, "en espera")
	estado = evento.wait()
	while contar < 25:
		contar+=1
		print(nom_hilo, ':', contar)


def main():
	evento = threading.Event()
	hilo1 = threading.Thread(name='h1', target=contar)
	hilo2 = threading.Thread(name='h2', target=contar)
	hilo1.start()
	hilo2.start()

	print('Obteniendo 25 números pares...')
	gen_pares()
	print('Ya se han obtenido')
	evento.set()


if __name__ == '__main__':
	main()