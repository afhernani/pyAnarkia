# -*- coding: utf-8 -*-

import tempfile

# Crea directorio temporal con gestor de contexto
with tempfile.TemporaryDirectory() as dirtemporal6:
    print('Directorio temporal', dirtemporal6)

# Al finalizar, tanto directorio como contenido se borran