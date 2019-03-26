import tkinter
from PIL import Image, ImageTk, ImageSequence

class App:
    def __init__(self, parent):
        self.parent = parent
        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(Image.open('./../work/Thumbails/candy.gif'))]
        self.img_width = self.sequence[0].width()
        self.img_height = self.sequence[0].height()
        print("w x h : {} x {}".format(self.img_width,self.img_width))
        self.canvas = tkinter.Canvas(self.parent, width=self.img_width, height=self.img_height, bg="yellow")
        self.canvas.pack()
        self.image = self.canvas.create_image(self.img_width/2, self.img_height/2, image=self.sequence[0])
        self.animating = True
        self.animate(0)

    def animate(self, counter):
        # print(counter)
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        if not self.animating:
            return
        self.parent.after(850, lambda: self.animate((counter+1)% len(self.sequence)))

def main():
    root = tkinter.Tk()
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()
