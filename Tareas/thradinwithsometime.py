'''
Hilos que funcionan durante un tiempo:
Otra opción interesante consiste en limitar el funcionamiento de los hilos a un tiempo
determinado.
En el ejemplo siguiente se inician 5 hilos que funcionan durante 1 segundo. Mientras transcurre
el tiempo cada hilo incrementa un contador hasta que se alcanza el tiempo límite. El módulo time
se utiliza para obtener el momento inicial y calcular el tiempo límite de ejecución.
Al concluir el tiempo de cada hilo el valor máximo contado se va añadiendo a un diccionario que
se muestra cuando el último hilo activo está finalizando. Para conocer cuándo está finalizando el
último hilo se utiliza la función threading.active_count() que devuelve el número de hilos que
aún quedan activos, incluyendo al hilo principal (que se corresponde con el hilo que inicia el
propio programa), es decir, cuando el último hilo Thread esté terminando quedarán activos 2
hilos. Para satisfacer la curiosidad al final se muestra una lista con información de estos hilos
obtenida con la función threading.enumerate().
La variable vmax_hilos contiene los valores máximos del contador de cada hilo. Esta variable se
inicializa al comienzo del programa y se declara después como global dentro de la función (Ver
variables locales y glboales). Esto se hace para lograr mantener "vivos" los valores máximos que
se añaden al diccionario al concluir cada hilo. Si no se declara como global sólo permanecerá el
último valor agregado.
'''
import threading, time

vmax_hilos = {}

def contar(segundos):
	"""Contar hasta un límite de tiempo"""
	global vmax_hilos
	contador = 0
	inicial = time.time()
	limite = inicial + segundos
	nombre = threading.current_thread().getName()
	while inicial<=limite:
		contador+=1
		inicial = time.time()
		print(nombre, contador)
	
	vmax_hilos[nombre] = contador
	if threading.active_count()==2:
		print(vmax_hilos)
		print(threading.enumerate())

		
def main():
	segundos = 1
	for num_hilo in range(5):
	hilo = threading.Thread(name='hilo%s' %num_hilo, 
							target=contar, 
							args=(segundos,))
	hilo.start()

if __name__ == '__main__':
	main()