### Modulo tempfile

    para este tipo de archivos temporales cuenta con el módulo tempfile que ofrece algunas ventajas interesantes al programador, en este ámbito
    
 ## Ventajas:
 
    crear archivos y directorios temporales
    Crea automáticamente y con seguridad los nombres de los archivos y directorios 
    Proporciona funciones que suprimen automáticamente los archivos y/o directorios temporales cuando ya no son necesarios. Estas funciones son TemporaryFile(), NamedTemporaryFile(), TemporaryDirectory() y SpooledTemporaryFile(). Además, para contar con mayor control sobre el borrado de los archivos y directorios temporales ofrece, alternativamente, las funciones mkstemp() y mkdtemp(), que requieren un borrado manual.
    
 ### TemporaryFile(). Crea archivo temporal (sin nombre)
 
    La función TemporaryFile() crea un archivo temporal de forma segura y devuelve un objeto (sin nombre) para ser utilizado como espacio de almacenamiento temporal y será suprimido tan pronto como sea cerrado. 
    
    tempfile.TemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
    
    Por defecto, la apertura del archivo temporal es "w+b" (lectura/escritura en modo binario) 
    
    Tambien se puede usar el modo "w+t" (lectura/escritura para textos).
    
    Los argumentos suffix y prefix, si se usan, se corresponden con la cadena de sufijo y/o de prefijo que se empleará en la construcción de los nombres de los archivos temporales. El argumento dir se utiliza para especificar un directorio para ubicar los archivos y en caso de que no se especifique ninguno se utilizará el directorio temporal del sistema, que suele ser el recomendado 
    
    En cuanto a los argumentos buffering, encoding y newline, tienen el mismo uso que con la función open(). Son para establecer la política de almacenamiento en el búfer, especificar un nombre de codificación de caracteres y fijar cómo será el salto de líneas en los archivos creados en modo texto
    
    Ejemplos: temporaryfile.py, temporaryfilewrong.py
    
### NamedTemporaryFile(). Crea archivo temporal (con nombre)

    La función NamedTemporaryFile() crea un archivo temporal al que asignará un nombre construido automáticamente, teniendo en cuenta en el caso de que se hayan utilizado, los argumentos suffix y prefix. 

    tempfile.NamedTemporaryFile(mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None, delete=True)

    Hay situaciones en las que es conveniente utilizar esta función que da nombre a los archivos temporales, como por ejemplo, cuando la información de estos archivos es utilizada por varios procesos diferentes. En ese caso la mejor referencia a utilizar será el propio nombre del archivo temporal para poder abrirlo, que puede obtenerse mediante el atributo name. Los archivos igualmente serán suprimidos cuando sean cerrados, excepto si al argumento delete se le asigna el valor False. 

    En cuanto a lo demás, esta función actúa exactamente igual que TemporaryFile(). 

    Ejemplo: nametemporaryfile.py
   
### SpooledTemporaryFile(). Crea archivo estableciendo tamaño máximo del búfer de memoria

    La función SpooledTemporaryFile() se utiliza para crear archivos temporales con un matiz que lo diferencia de la función TemporaryFile(). Incorpora el argumento max_size para establecer el tamaño máximo de memoria que se usará para almacenar el archivo temporal. 

    Cuando el límite de max_size sea superado, o bien, cuando sea llamado el metodo fileno() los datos pasarán a escribirse directamente al disco. 

    tempfile.SpooledTemporaryFile(max_size=0, mode='w+b', buffering=None, encoding=None, newline=None, suffix=None, prefix=None, dir=None)
    
    Ejemplo: spoledtemporaryfile.py
    
### TemporaryDirectory(). Crea directorio temporal

    La función TemporaryDirectory() crea un directorio temporal cuyo nombre puede ser recuperado accediendo al valor del atributo name. El objeto resultante se puede utilizar como un gestor de contexto que termina suprimiendo el directorio y todo su contenido. 

    En el siguiente ejemplo se crea un directorio temporal utilizando la declaración "with ... as" como gestor de contexto:

<code>

    import tempfile
    #Crea directorio temporal con gestor de contexto
    with tempfile.TemporaryDirectory() as dirtemporal6:
        print('Directorio temporal', dirtemporal6)
    # Al finalizar, tanto directorio como contenido se borran

 </code>
 
    Emjemplo: temporarydir.py, temporarydirname.py
 
### mkstemp(). Crea archivo temporal sin borrado desatendido

    La función mkstemp() crea con seguridad un archivo temporal en la que la operación de borrado queda a elección del usuario. 

    tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False) 

    Devuelve una tupla que contiene un identificador (como el que devuelve la función os.open()) y la ruta de acceso absoluta al archivo temporal. 

    A partir de Python 3.5 los argumentos suffix, prefix y dir pueden expresarse como bytes.
    
    Ejemplo: mkstemp.py 

### mkdtemp(). Crea directorio temporal sin borrado desatendido

    La función mkdtemp() crea con seguridad un directorio temporal en la que la operación de borrado no es desatendida. El usuario, cuando lo desee, tendrá que realizarla "manualmente". 

    tempfile.mkdtemp(suffix=None, prefix=None, dir=None)

    La función mkdtemp() devuelve la ruta absoluta del directorio temporal 

    A partir de Python 3.5 los argumentos suffix, prefix y dir pueden expresarse como bytes. 

    Ejemplo: mkdtemp.y
    
    
### gettempdir()/gettempdirb(). Obtiene directorio temporal

    Las funciones gettempdir() y gettempdirb() devuelven la ruta del directorio temporal del sistema (/tmp, c:\temp, etc.). La primera función la devuelve en formato str y la segunda expresada como bytes
    
    print("Dir temporal del sistema", tempfile.gettempdir())
    print("Dir temporal (en bytes)", tempfile.gettempdirb())  # Python +3.5

### gettempprefix()/gettempprefixb(). Obtiene prefijos de nombres

    Las funciones gettempprefix() y gettempprefixb() devuelven los prefijos que se aplican a los nombres de los archivos temporales, en el momento de su creación. La primera función la devuelve como str y la segunda como bytes.

    print("Prefijo", tempfile.gettempprefix())
    print("Prefijo (en bytes)", tempfile.gettempprefixb())  # Python +3.5
    
    
### La variable tempdir

    La variable global tempdir almacena el directorio temporal predeterminado del sistema, que es el mismo que devuelven las funciones gettempdir() y gettempdirb(). Este directorio puede cambiarse asignándose una nueva ruta a dicha variable, aunque no se recomienda. 

    En el supuesto de que se modifique la ruta, será la que se utilice en todas las funciones de este modulo como predeterminada para el argumento dir.

    tempfile.tempdir = '/home/usuario/temp'
    print("Directorio temporal", tempfile.gettempdir())
    print("Directorio temporal", tempfile.tempdir)

