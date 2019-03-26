# -*- coding:UTF-8 -*-
import os
from typing import List

listas = []
videos = []


def load_name_file_gif():
    listas = os.listdir(r'imagen')
    print(listas)
    for item in listas:
        div = item.split("_thumbs_")
        print('fichero: ', div[0])
        videos.append(div[0])


def main():
    load_name_file_gif()
    print(videos)


if __name__ == '__main__':
    main()