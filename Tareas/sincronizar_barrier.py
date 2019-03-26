'''
Sincronizar hilos con objetos Barrier.
Los objetos barrera (Barrier) son otro mecanismo de sincronización de hilos. Como su propio
nombre sugiere actúan como una verdadera barrera que mantiene los hilos bloqueados en un
punto del programa hasta que todos hayan alcanzado ese punto.
En el siguiente ejemplo se inician cinco hilos que obtienen un número aleatorio y permanecen
bloqueados en el punto donde se encuentra el método wait() a la espera de que el último hilo
haya obtenido su número. Después, continúan todos mostrando el factorial del número obtenido
en cada caso.
'''
import threading, random, math

def funcion1(barrera):
	nom_hilo = threading.current_thread().name
	print(nom_hilo,
		'Esperando con',
		barrera.n_waiting,
		'hilos más')
	numero = random.randint(1,10)
	ident = barrera.wait()
	print(nom_hilo,
		'Ejecutando después de la espera',
		ident)
	print('factorial de',
		numero,
		'es',
		math.factorial(numero))


NUM_HILOS = 5

def main():
	barrera = threading.Barrier(NUM_HILOS)
	hilos = [threading.Thread(name='hilo-%s' % i,
							target=funcion1,
							args=(barrera,),
							) for i in range(NUM_HILOS)]
	for hilo in hilos:
		print(hilo.name, 'Comenzando ejecución')
		hilo.start()

if __name__ == '__main()__':
	main()

	
'''
Existe la posibilidad de enviar un aviso de cancelación a todos los hilos que esperan con el
método  abort()  del  objeto  Barrier.  Esta  acción  genera  una  excepción  de  tipo
threading.BrokenBarrierError que se debe capturar y tratar convenientemente:

try:
	ident = barrera.wait()
except threading.BrokenBarrierError:
	print(nom_hilo, 'Cancelando')
else:
	print('Ejecutando después de la espera', ident)
	
'''