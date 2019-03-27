# -*- encoding: utf-8 -*-

import tempfile

"""
A continuación, un ejemplo en el que se une la creación de un directorio 
temporal con un archivo temporal y que finaliza con la supresión de ambos:

"""

# Crea directorio temporal
tempdir7 = tempfile.TemporaryDirectory()

# Crea archivo temporal en el directorio anterior
temporal7 = tempfile.NamedTemporaryFile(dir=tempdir7.name)

# Muestra nombres de directorio y archivo temporales
print('Directorio temporal:', tempdir7.name)
print('Archivo temporal...:', temporal7.name)

# Escribe en el archivo
for ciclo in range(0,50000):
    temporal7.write(b"=" * 20)

# Borra archivo temporal
del temporal7

# Borra directorio temporal
del tempdir7