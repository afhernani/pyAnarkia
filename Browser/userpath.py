#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
import os
import pwd


def get_username():
    return pwd.getpwuid(os.getuid())[0]
'''
import os
import getpass
import platform
from pathlib import Path

print(Path.home())
print(os.getenv('HOME'))
# El nombre del usuario
print(getpass.getuser())

# El nombre del PC
print(platform.node())
