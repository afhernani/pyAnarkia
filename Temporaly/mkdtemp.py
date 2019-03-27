# -*- encoding: utf-8 -*-
"""
Uso de la función mkdtemp():

"""
import os, tempfile

# Crea directorio temporal con el prefijo 'Aplic'
tempdir9 = tempfile.mkdtemp(prefix='Aplic')

# Muestra directorio creado
print(tempdir9)

# Borra directorio tempora si existe
if os.path.exists(tempdir9):
    os.rmdir(tempdir9)
    print('Directorio suprimido')