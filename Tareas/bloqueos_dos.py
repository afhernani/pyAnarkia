'''
Bloqueo:
Para conocer si otro hilo ha adquirido el bloqueo sin mantener al resto de subprocesos detenidos
hay que asignar al argumento blocking de acquire() el valor False. De esta forma se pueden
realizar otros trabajos mientras se espera a tener éxito en un bloqueo y controlar el número de
reintentos realizados. El método locked() se puede utilizar para verificar si un bloqueo se
mantiene en un momento dado:
'''
import threading

def acumula5():
	global total
	contador = 0
	hilo_actual = threading.current_thread().getName()
	num_intentos = 0
	while contador < 20:
		lo_consegui = bloquea.acquire(blocking=False)
		try:
			if lo_consegui:
				contador = contador + 1
				total = total + 5
				print('Bloqueado por', hilo_actual, contador)
				print('Total', total)
			else:
				num_intentos+=1
				print('Número de intentos de bloqueo',
					num_intentos,
					'hilo',
					hilo_actual,
					bloquea.locked())
				print('Hacer otro trabajo')
				
		finally:
			if lo_consegui:
				print('Liberado bloqueo por', hilo_actual)
				bloquea.release()

# variables globales.
total = 0
bloquea = threading.Lock()

def main():
	hilo1 = threading.Thread(name='h1', target=acumula5)
	hilo2 = threading.Thread(name='h2', target=acumula5)
	hilo1.start()
	hilo2.start()

if __name__ == '__main__':
	main()