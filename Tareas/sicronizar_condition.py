'''
Sincronizar hilos con objetos condition:
Los objetos Condition se utilizan también para sincronizar la ejecución de varios hilos. En este
caso los bloqueos suelen estar vinculados con unas operaciones que se tienen que realizar antes
que otras.
En el siguiente ejemplo un hilo espera -llamando al método wait()- a que otro hilo genere mil
números aleatorios que son añadidos a una lista. Una vez que se han obtenido los números el
hecho es notificado con notifyAll() al hilo que espera. Finalmente, el hilo detenido continua su
ejecución mostrando el número de elementos generados y la suma de todos ellos, con la función
fsum() del módulo math.
'''
import threading, random, math

def funcion1(condicion):
	global lista
	print(threading.current_thread().name,
		'esperando a que se generen los números')
	with condicion:
		condicion.wait()
		print('Elementos:', len(lista))
		print('Suma total:', math.fsum(lista))

def funcion2(condicion):
	global lista
	print(threading.current_thread().name,
		'generando números')
	with condicion:
		for numeros in range(1, 1001):
			entero = random.randint(1,100)
			lista.append(entero)
		print('Ya hay 1000 números')
		condicion.notifyAll()


def main():
	lista = []
	condicion = threading.Condition()
	hilo1 = threading.Thread(name='hilo1', target=funcion1, args=(condicion,))
	hilo2 = threading.Thread(name='hilo2', target=funcion2, args=(condicion,))
	hilo1.start()
	hilo2.start()

if __name__ == '__main__':
	main()