#!/usr/bin/python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import os
"""
 Ejemplo de iteracion sobre un listbox
"""
class GUI():
    def __init__(self,frame): # Some Init
        self.yscrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
        self.xscrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL)
        self.listbox = tk.Listbox(root, height=20, width=51, selectmode=tk.SINGLE, exportselection=0, yscrollcommand=self.yscrollbar.set, xscrollcommand=self.xscrollbar.set)
        # -- Some Grid setup here --
        self.listbox.bind("<<ListboxSelect>>", self.selectionCallback)
        self.listbox.bind("<Shift-A>", self.shiftCallback)
        self.listbox.bind("<KeyRelease>", self.keyrelease)
        self.listbox.bind("<Return>", self.returnkey)
        self.listbox.bind("<Key>", self.presskey)
        self.listbox.bind('<ButtonRelease-1>', self.buttonrelease)
        
        self.yscrollbar.pack(side=tk.RIGHT, fill= tk.Y)
        self.xscrollbar.pack(side=tk.BOTTOM, fill = tk.X)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.listbox.focus_set()
        for item in ["one", "two", "three", "four"]:
            self.listbox.insert(tk.END, item) 
        self.listbox.selection_set(0)

    def keyrelease(self, event):
        print('keyrelease ->', event)

    def buttonrelease(self, event):
        '''
        seleccionar con el raton con un solo click
        '''
        print('buttonrelease ->', event)
        item = self.listbox.nearest(event.y)
        print('valor =', self.listbox.get(item))

    def selectionCallback(self, event):
        print('selectioncallback ->', self.listbox.get(tk.ACTIVE))
        w=event.widget
        index = int(w.curselection()[0])
        value=w.get(index)
        print('selecionado ->', value)

    def shiftCallback(self, event):
        print('shiftcallback ->', event)
        if event.type is 2: #KeyPress
            self.shift = True
        elif event.type is 3: #KeyRelease
            self.shift = False

    def returnkey(self, key):
        print('returnkey ->',key)
        item = self.listbox.curselection()[0]
        print('item ->',self.listbox.get(item))

    def presskey(self, event):
        print('presskey ->', event)
        print('len = ', len(self.listbox.get(0,'end'))-1)
        w=event.widget
        index = int(w.curselection()[0])
        value=w.get(index)
        print('valor =', value)
        iter = 0
        if event.keysym == 'Up' and index > 0:
            iter = index-1
            self.listbox.selection_clear(index)
            self.listbox.selection_set(iter)
            print("selected ->", w.get(iter))
        if event.keysym == 'Down' and index < (len(self.listbox.get(0,'end'))-1):
            iter = index+1
            self.listbox.selection_clear(index)
            self.listbox.selection_set(iter)
            print("selected ->", w.get(iter))
        

if __name__ == "__main__":
    root = tk.Tk()
    GUI(root)
    root.mainloop()

