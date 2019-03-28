#!/usr/bin/python3
# -*- coding: utf-8 -*-

import configparser

def configwrite():
    '''
    An example of writing to a configuration file:
    '''
    config = configparser.RawConfigParser()

    # Please note that using RawConfigParser's set functions, you can assign
    # non-string values to keys internally, but will receive an error when
    # attempting to write to a file or when you get it in non-raw mode. Setting
    # values using the mapping protocol or ConfigParser's set() does not allow
    # such assignments to take place.
    config.add_section('Section1')
    config.set('Section1', 'an_int', '15')
    config.set('Section1', 'a_bool', 'true')
    config.set('Section1', 'a_float', '3.1415')
    config.set('Section1', 'baz', 'fun')
    config.set('Section1', 'bar', 'Python')
    config.set('Section1', 'foo', '%(bar)s is %(baz)s!')

    # Writing our configuration file to 'example.cfg'
    with open('example.ini', 'w') as configfile:
        config.write(configfile)


def configread():
    '''
    An example of reading the configuration file again
    '''
    config = configparser.RawConfigParser()
    config.read('example.ini')
    
    # getfloat() raises an exception if the value is not a float
    # getint() and getboolean() also do this for their respective types
    a_float = config.getfloat('Section1', 'a_float')
    an_int = config.getint('Section1', 'an_int')
    print(a_float + an_int)
    # cambiamos un valor del registro.
    config.set('Section1', 'an_int', '1000')
    #escribimos al registro.
    config.write(open('example.ini', 'w'))
    # Notice that the next output does not interpolate '%(bar)s' or '%(baz)s'.
    # This is because we are using a RawConfigParser().
    if config.getboolean('Section1', 'a_bool'):
        print(config.get('Section1', 'foo'))


def interpolation():
    cfg = configparser.ConfigParser()
    cfg.read('example.ini')
    
    # Set the optional *raw* argument of get() to True if you wish to disable
    # interpolation in a single get operation.
    print(cfg.get('Section1', 'foo', raw=False))  # -> "Python is fun!"
    print(cfg.get('Section1', 'foo', raw=True))   # -> "%(bar)s is %(baz)s!"
    
    # The optional *vars* argument is a dict with members that will take
    # precedence in interpolation.
    print(cfg.get('Section1', 'foo', vars={'bar': 'Documentation',
                                           'baz': 'evil'}))
    
    # The optional *fallback* argument can be used to provide a fallback value
    print(cfg.get('Section1', 'foo'))
          # -> "Python is fun!"
    
    print(cfg.get('Section1', 'foo', fallback='Monty is not.'))
          # -> "Python is fun!"
    
    print(cfg.get('Section1', 'monster', fallback='No such things as monsters.'))
          # -> "No such things as monsters."
    
    # A bare print(cfg.get('Section1', 'monster')) would raise NoOptionError
    # but we can also use:
    
    print(cfg.get('Section1', 'monster', fallback=None))
          # -> None

def interpolation_not_definided():
    '''
    Default values are available in both types of ConfigParsers. 
    They are used in interpolation if an option used is not defined elsewhere.
    '''
    # New instance with 'bar' and 'baz' defaulting to 'Life' and 'hard' each
    config = configparser.ConfigParser({'bar': 'Life', 'baz': 'hard'})
    config.read('example.ini')
    
    print(config.get('Section1', 'foo'))     # -> "Python is fun!"
    config.remove_option('Section1', 'bar')
    config.remove_option('Section1', 'baz')
    print(config.get('Section1', 'foo'))     # -> "Life is hard!"


def readline_generator(fp):
    '''
    Instead of parser.readfp(fp) use parser.read_file(readline_generator(fp)).
    '''
    line = fp.readline()
    while line:
        yield line
        line = fp.readline()


if __name__ == '__main__':
    configwrite()
    configread()
    interpolation()
    interpolation_not_definided()
