# -*- coding:UTF-8 -*-
import tkinter as tk
import os
from spritepane import SpritePane
from tkinter import ttk
from PIL import Image, ImageTk, ImageSequence


class Flowlayout(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title('Flowlayout')
        self.parent.iconbitmap('./../ico/super.ico')
        self.parent['bg']= 'Yellow'
        self.pack(fill=tk.BOTH, expand=1)
        self.textwidget= tk.Text(self, bg='Black')
        self.textwidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.scrolbar = tk.Scrollbar(self.textwidget, orient='vertical', command=self.textwidget.yview)
        self.textwidget.configure(yscrollcommand=self.scrolbar.set)
        self.scrolbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.bind_all("<MouseWheel>", self.mouse_scroll)
        self.bind_all("<Button-4>", self.mouse_scroll)
        self.bind_all("<Button-5>", self.mouse_scroll)
        self.load_from_file()
        #self.load_from_file_img()

    def load_from_file(self):
        for fe in os.listdir('./../work/Thumbails'):
            if fe.endswith(".gif") or fe.endswith(".jpg"):
                fex = os.path.abspath(os.path.join('./../work/Thumbails', fe))
                print(fex)
                self.textwidget.window_create(tk.INSERT, window=self.load_sprite(arg=fex))

    def load_from_file_img(self):
        for fe in os.listdir('./../work/Thumbails'):
            if fe.endswith(".gif") or fe.endswith(".jpg"):
                fex = os.path.abspath(os.path.join('./../work/Thumbails', fe))
                print(fex)
                self.textwidget.window_create(tk.INSERT,
                                              window=self.load_sprite(fex))

    def load_sprite(self, arg):
        if not os.path.isfile(arg):
            print("is not a file")
        return SpritePane(self.textwidget, fileImagen=arg)

    def mouse_scroll(self, event):
        print('mouse_scroll_control')
        if event.delta:
            self.textwidget.yview_scroll(int(-1*(event.delta/120)), "units")
        else:
            if event.num == 5:
                move = 1
            else:
                move = -1
                self.textwidget.yview_scroll(move, "units")


def main():
    root = tk.Tk()
    root.geometry("800x600")
    app = Flowlayout(parent=root)
    app.mainloop()


if __name__ == '__main__':
    main()
