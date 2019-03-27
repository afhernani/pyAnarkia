#!bin/python
# -*- encoding: utf-8 -*-
"""
El siguiente ejemplo crea archivo temporal limitando la memoria a 1024 bytes:
"""

import tempfile

# Crea archivo temporal fijando búfer en 1024 bytes
temporal4 = tempfile.SpooledTemporaryFile(max_size=1024)

# Escribe en el fichero temporal
for ciclo in range(0,20):
    temporal4.write((b"*" * 50) + b"\n")

# Sitúa el puntero al comienzo del archivo temporal
temporal4.seek(0)

# Lee el archivo temporal
lectura4 = temporal4.read()

# Convierte la cadena leida de byte a string con codificación utf-8
print(lectura4.decode("utf-8"))

# Muesta idenfiticador del archivo cuando supere el límite de
# max_size. En caso contrario, el valor devuelto será None porque
# el archivo sólo se alojará en la memoria. Para probar otros resultados
# modificar el valor de max_size, por ejemplo, reduciéndolo
print(temporal4.name)

# Muestra la longitud de la cadena leída
print(len(lectura4))

# Cierra y elimina el archivo temporal
temporal4.close()