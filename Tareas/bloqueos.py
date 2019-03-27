'''
Control del acceso a los recursos. Bloqueos.
Además de sincronizar el funcionamiento de varios subprocesos también es importante controlar
el acceso de los hilos a los recursos compartidos (variables, listas, diccionarios, etc.) para evitar
la corrupción o pérdida de datos. En determinadas circunstancias estas estructuras de datos
requieren protegerse con bloqueos contra el acceso simultáneo de varios hilos que intentan
modificar su valores. Esto raramente va a suceder si varios hilos tratan de actualizar una sola
variable. Sin embargo, el problema se puede dar al actualizar el valor de una variable que utiliza
los datos de otras variables (intermedias) que son leídas y modificadas varias veces en el
proceso por varios hilos.
Los objetos Lock permiten gestionar los bloqueos que evitan que los hilos modifiquen variables
compartidas al mismo tiempo. El método acquire() permite que un hilo bloquee a otros hilos en
un punto del programa, donde se leen y actualizan datos, hasta que dicho hilo libere el bloqueo
con el método release(). En el momento que se produzca el desbloqueo otro hilo (o el mismo)
podrá bloquear de nuevo.
En el ejemplo que sigue se inician dos hilos que actualizan la variable global total donde se van
acumulando números que son múltiplos de 5. Antes y después de cada actualización se produce
un bloqueo y un desbloqueo, respectivamente:
'''
import threading

total = 0
bloquea = threading.Lock()

def acumula5():
	global total
	global bloquea
	contador = 0
	hilo_actual = threading.current_thread().getName()
	while contador < 20:
		print('Esperando para bloquear', hilo_actual)
		bloquea.acquire()
		try:
			contador = contador + 1
			total = total + 5
			print('Bloqueado por', hilo_actual, contador)
			print('Total', total)
			
		finally:
			print('Liberado bloqueo por', hilo_actual)
			bloquea.release()


def main():
	#bloquea = threading.Lock()
	hilo1 = threading.Thread(name='h1', target=acumula5)
	hilo2 = threading.Thread(name='h2', target=acumula5)
	hilo1.start()
	hilo2.start()

if __name__ == '__main__':
	main()