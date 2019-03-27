#!bin/
# -*- encoding: utf-8 -*-

'''
El siguiente ejemplo muestra cómo crear un
archivo temporal con la función TemporaryFile(), en modo binario:
'''
import tempfile

# Crea un archivo temporal en modo binario
temporal1 = tempfile.TemporaryFile()

# Muestra información del objeto creado
print(temporal1)  # _io .bufferedrandom="" name="4"
print(type(temporal1))  # class io.bufferedrandom=""
print(temporal1.name)  # identificador del archivo, 4

# Escribe en el fichero temporal
temporal1.write(b'archivos temporales\ncon Python')

# Sitúa el puntero al comienzo del archivo
temporal1.seek(0)

# Lee archivo temporal desde su comienzo
lectura1 = temporal1.read()

# Muestra la información leída
print(lectura1)

# Cierra y elimina el archivo temporal
temporal1.close()