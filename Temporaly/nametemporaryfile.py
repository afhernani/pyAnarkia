#!bin/python
# -*- encoding: utf-8 -*-
"""

Ejemplo de uso de la función NamedTemporaryFile()

"""
import os, tempfile

# Crea archivo temporal
temporal3 = tempfile.NamedTemporaryFile()

# Muestra nombre y ruta del archivo temporal creado
print(temporal3, temporal3.name)

# Escribe en el archivo temporal
temporal3.write(b'Temporal')

# Comprueba si existe el archivo temporal
if os.path.exists(temporal3.name):
    print("El archivo temporal existe")

# Cierra y suprime el archivo temporal
temporal3.close()

# Comprueba si se ha borrado el archivo temporal
if not os.path.exists(temporal3.name):
    print("El archivo temporal ya no existe")
