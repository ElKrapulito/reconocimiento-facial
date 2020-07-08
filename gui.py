import os
from tkinter import *
from PIL import ImageTk,Image
import lookImage as mimg

# BASE_DIR = os.path.dirname(os.path.abspath(__file__)) +'\images'

def loopDirectory(directory):
    dirs = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpeg") or filename.endswith(".png") or filename.endswith(".jpg"): 
            # dirs.append(os.path.join(directory, filename))
            dirs.append(filename)
            continue
        else:
            continue
    return dirs

def execNewImage():
    mimg.detectFace(clicked.get())
def openWebCamNow():
    mimg.openWebCam()
def refresh():
    drop.pack_forget()
    name_images = loopDirectory('.\\images')
    drop = OptionMenu(root, clicked, *name_images).pack()

name_images = loopDirectory('.\\images')
root = Tk()
root.title('Imagenes')

clicked = StringVar()
clicked.set(name_images[0])


myButton = Button(root,text='Seleccionar Imagen',command=execNewImage).pack()
myButton1 = Button(root,text='Web Cam',command=openWebCamNow).pack()
myButton2 = Button(root,text='Refresh',command=refresh).pack()
drop = OptionMenu(root, clicked, *name_images)
drop.pack()


root.mainloop()