'''
Temporizadores:
Un temporizador (Timer) es un tipo de hilo especial que permite ajustar el comienzo de su
ejecución con un tiempo de espera. Además, mientras transcurre este tiempo de espera es
posible cancelar su ejecución.
Un temporizador es un objeto de la subclase Timer que deriva de la clase Thread y como sucede
con sus ancestros admite el paso de argumentos:
class threading.Timer(intervalo, función, args=None, kwargs=None)
En el siguiente ejemplo se crean dos temporizadores (hilo1 y hilo2) con un tiempo de espera de
0.2 y 0.5 segundos, respectivamente. Cuando se cumple el tiempo de espera de hilo1 comienza
su ejecución. Sin embargo, hilo2 es cancelado antes de concluir su tiempo de espera. El
programa termina cuando hilo1 finaliza su trabajo.
'''
import threading
import time

def retrasado():
	nom_hilo = threading.current_thread().getName()
	contador = 1
	while contador <=10:
		print(nom_hilo, 'ejecuta su trabajo', contador)
		time.sleep(0.1)
		contador+=1
	print(nom_hilo, 'ha terminado su trabajo')


def main():	
	hilo1 = threading.Timer(0.2, retrasado)
	hilo1.setName('hilo1')
	hilo2 = threading.Timer(0.5, retrasado)
	hilo2.setName('hilo2')

	hilo1.start()
	hilo2.start()
	print('hilo1 espera 0.2 segundos')
	print('hilo2 espera 0.5 segundos')

	time.sleep(0.3)
	print('hilo2 va a ser cancelado')
	hilo2.cancel()
	print('hilo2 fue cancelado antes de iniciar su ejecución')

if __name__ == '__main__':
	main()