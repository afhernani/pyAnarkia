#!/bin/python
# -*- coding: UTF-8 -*-
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS

def others():
    import exif
    photo_path = "america.jpg"
    data = exif.parse(photo_path)

def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def main():
    #get_exif("america.jpg")
    others()
    """
    img = Image.open("america.jpg")
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
    print(exif)
    """

if __name__ == '__main__':
    main()
