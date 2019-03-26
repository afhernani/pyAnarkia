#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from os import listdir, sep, environ
from os.path import isdir, join, abspath
from pathlib import Path
from threeview import Treeviewhome


class Application(ttk.Frame):

    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Explorador de archivos y carpetas")

        self.tree = Treeviewhome(main_window)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.datos = tk.StringVar()
        self.textbox = tk.Text(main_window, width=20, height= 60, bg='white', fg='black')
        self.textbox.grid(row=0, column=1)
        #Asociacion de eventos
        self.tree.bind("<Button-1>", self.opened_item)
        self.tree.bind("<Enter>", self.opened_item)
        self.textbox.bind("<Key>", self.key)
        #Asocia con la clase hija.
        self.tree.bind_class("Treeview", "<<TreeviewOpen>>", self.item_opened)

    def opened_item(self, event):
        """
        Evento invocado cuando el contenido de una carpeta es abierto.
        """
        print("opened_item")
        '''
        if self.tree.treeview.curselection():
            file = self.tree.treeview.curselection()[0]
            # os.system("ffplay " + lb.get(file))
            #thread = Thread(target=tarea, args=("ffplay " + lb.get(file),))
            #thread.daemon = True
            #thread.start()
        '''

    def item_opened(self, event):
            iid = self.tree.treeview.selection()[0]
            iis = self.tree.fsobjects[iid]
            self.textbox.insert(tk.INSERT, iid + '\n' + iis + '\n')
            print(self.textbox.get(1.0, tk.END))

    def key(self, event):
        print("pressed", repr(event.char))


def main():
    main_window = tk.Tk()
    main_window.geometry("400x600")
    app = Application(main_window)
    app.mainloop()


if __name__ == '__main__':
    main()
