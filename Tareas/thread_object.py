'''
Objetos Thread: los hilos.
En Python un objeto Thread representa una determinada operación que se ejecuta como un
subproceso independiente, es decir, representa a un hilo. Hay dos formas de definir un hilo: la
primera, consiste en pasar al método constructor un objeto invocable, como una función, que es
llamada cuando se inicia la ejecución del hilo y, la segunda, radica en crear una subclase de
Thread en la que se reescribe el método run() y/o el constructor __init__().
En el siguiente ejemplo se crean dos hilos que llaman a la función contar. En dicha función se
utiliza la variable contador para contar hasta cien. Los objetos Thread (los hilos) utilizan el
argumento target para establecer el nombre de la función a la que hay que llamar. Una vez que
los hilos se han creado se inician con el método start(). A todos los hilos se les asigna,
automáticamente, un nombre en el momento de la creación que se puede conocer con el método
getName() y, también, un identificador único (en el momento que son iniciados) que se puede
obtener accediendo al valor del atributo ident:
'''
import threading

def contar():
	'''Contar hasta cien'''
	contador = 0
	while contador<100:
		contador+=1
		print('Hilo:',
				threading.current_thread().getName(),
				'con identificador:',
				threading.current_thread().ident,
				'Contador:', contador)


def main():
	hilo1 = threading.Thread(target=contar)
	hilo2 = threading.Thread(target=contar)
	hilo1.start()
	hilo2.start()

if __name__ == '__main__':
	main()