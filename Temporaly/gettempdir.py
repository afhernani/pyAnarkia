# -*- encoding: utf-8 -*-
import tempfile

print("Dir temporal del sistema", tempfile.gettempdir())
print("Dir temporal (en bytes)", tempfile.gettempdirb())  # Python +3.5

print("Prefijo:", tempfile.gettempprefix())
print("Prefijo (en bytes)", tempfile.gettempprefixb())  # Python +3.5

#tempfile.tempdir = '/home/usuario/temp'
print("Directorio temporal", tempfile.gettempdir())
print("Directorio temporal", tempfile.tempdir)