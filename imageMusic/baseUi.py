import sys
import os

from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

def UploadAction(event = None):
    filename = filedialog.askopenfilename()
    print('Selected:', filename)
    load = Image.open(filename)
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=0, y=0)

def gui(title, message):
    root = Tk()
    root.title(title)

    w= 450
    h= 300
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2

    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    m = message
    m += '\n'

    w = Label(root, text=m, width=120, height=10)
    w.pack()
    importbut = Button(root, text="Import", command=UploadAction, width=10)
    importbut.pack()

    mainloop()

gui("GUI.pi", "Import an image file.")
