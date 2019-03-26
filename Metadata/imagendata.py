#!/bin/python
# -*- coding: UTF-8 -*-
import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

def main():
    """
        import sys
        print "This is the name of the script: ", sys.argv[0]
        print "Number of arguments: ", len(sys.argv)
        print "The arguments are: " , str(sys.argv)
    """
    if len(sys.argv) <= 1 :
        print("incluir argumento: nombre fichero imagen")
        return 0
    img = sys.argv[2]
    image = sys.argv[2]

    for (tag,value) in Image.open(image)._getexif().iteritems():
            print ('%s = %s' % (TAGS.get(tag), value))

if __name__ == '__main__':
    main()
