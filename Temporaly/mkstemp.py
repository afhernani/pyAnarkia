# -*- encoding: utf-8 -*-
"""
En el siguiente ejemplo se crea un archivo temporal que
es borrado "manualmente" con el método os.remove().
"""
import os, tempfile

id8, archivotemp8 = tempfile.mkstemp(prefix="TempDirApp", text=True)

print("idenfificador:", id8)
print("archivo:", archivotemp8)

os.remove(archivotemp8)
if not os.path.exists(archivotemp8):
    print("El archivo {} ha sido borrado\n".format(archivotemp8))
