# _*_ coding: UTF-8 _*_

from tkinter import *
import csv
from tkinter import filedialog


class Window:
    def __init__(self, master):
        self.master = master
        self.filename = ""
        self.entryText = StringVar()
        self.csvfile = Label(self.master, text="Load File:").grid(row=1, column=0)
        self.bar = Entry(self.master, textvariable=self.entryText).grid(row=1, column=1)

        # Buttons
        y = 12
        self.cbutton = Button(self.master, text="OK", command=self.process_csv)
        y += 1
        self.cbutton.grid(row=15, column=3, sticky=W + E)
        self.bbutton = Button(self.master, text="File Browser", command=self.browsecsv)
        self.bbutton.grid(row=1, column=3)

    def browsecsv(self):
        Tk().withdraw()
        self.filename = filedialog.askopenfilename()
        self.entryText.set(self.filename)
        print(self.filename)

    @staticmethod
    def callback():
        pass
        '''
        abc = askopenfilename()
        execfile("input.xlsx")
        '''

    def process_csv(self):
        if self.filename:
            with open(self.filename, 'rb') as csvfile:
                logreader = csv.reader(csvfile, delimiter=',', quotechar='|')
                rownum = 0

                for row in logreader:
                    numcolumns = len(row)
                    rownum += 1

                matrix = [[0 for x in range(numcolumns)], [0 for x in range(rownum)]]
                print(matrix)


def main():
    root = Tk()
    window = Window(root)
    root.mainloop()


if __name__ == '__main__':
    main()

'''


Your both questions are connected. The problem is in your browsecsv(self) method. Your directory is already stored in self.filename, no need to call askopenfilename() again. That's the reason why the file browser opens twice. Moreover, to set text in your Entry, you need to assign it a text variable.

self.entryText = StringVar()
self.bar = Entry(root, textvariable=self.entryText ).grid(row=1, column=1)

Then, you can assign it to the Entry in your method:

def browsecsv(self):
   from tkFileDialog import askopenfilename
   Tk().withdraw() 
   self.filename = askopenfilename()
   self.entryText.set(self.filename)
'''
