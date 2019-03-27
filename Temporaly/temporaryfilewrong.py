#!/bin/python
# -*- encoding: utf-8 -*-

"""
En el ejemplo que sigue se muestra cómo crear un archivo temporal en modo texto,
con la posibilidad de capturar los errores que pudieran producirse al acceder
al sistema de archivos:
"""

import tempfile

# Crea un archivo temporal en modo texto
temporal2 = tempfile.TemporaryFile(mode='w+t')
print(temporal2.name)  # identificador del archivo, 4

# Captura posibles errores de acceso al sistema de archvios
try:
    # Escribe tres líneas en el archivo temporal
    temporal2.writelines(['Linea 1\n', 'Linea 2\n', 'Linea 3\n'])

    # Sitúa el puntero al comienzo del archivo
    temporal2.seek(0)

    # Lee y muestra todas las líneas del archivo temporal
    for linea in temporal2:
        print(linea.rstrip())

finally:
    # Cierra y elimina el archivo temporal
    temporal2.close()
