# _*_ coding:UTF-8 _*_
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import os


class SpritePane:
    def __init__(self, parent, fileImagen=None, timer=None):
        self.parent = parent
        self.fileImagen = fileImagen
        print('file path: ', self.fileImagen)
        if not fileImagen:
            self.fileImagen = './../work/Thumbails/candy.flv_thumbs_0000.gif'
            print('file abspath: ', os.path.abspath(self.fileImagen))
        # else:
        #    self.fileImagen= os.path.abspath(fileImagen)
        self.timer = timer
        if not timer:
            self.timer = 850
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open(self.fileImagen))]
        self.img_width = self.sequence[0].width()
        self.img_height = self.sequence[0].height()
        print("w x h : {} x {}".format(self.img_width, self.img_width))
        self.canvas = tk.Canvas(self.parent, width=self.img_width, height=self.img_height, bg="yellow")
        self.canvas.pack()
        self.image = self.canvas.create_image(self.img_width / 2, self.img_height / 2, image=self.sequence[0])
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)
        self.animating = True
        # self.animate(0)
        self.index = 0

    def animate(self, counter):
        # print(counter)
        self.index = counter
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.parent.after(self.timer, lambda: self.animate((counter + 1) % len(self.sequence)))

    def enter(self, event):
        self.animating = True
        self.animate(self.index)

    def leave(self, event):
        self.animating = False


def main():
    root = tk.Tk()
    root.geometry("400x600")
    app = SpritePane(root)  # , fileImagen=r'cotton.gif', timer=200)
    app2 = SpritePane(root, fileImagen='./../work/Thumbails/cotton.gif')
    # app3 = SpritePane(root, fileImagen=r'work\Thumbails\rosa.gif')
    # app4 = SpritePane(root, fileImagen=r'work\Thumbails\catty.gif')
    root.mainloop()


if __name__ == '__main__':
    print('directorio trabajo -> ', os.getcwd())
    main()
