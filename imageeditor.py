from tkinter import *
from PIL import ImageTk,Image,ImageOps,ImageEnhance
from tkinter import filedialog
from tkinter import messagebox

win=Tk()
win.geometry("900x700")

win.title("image editor")
img=Image.open("b1.jpg")
img=img.resize((600,600))

def displayimage (img):
    dimg=ImageTk.PhotoImage(img)
    pannel.configure(image=dimg)
    pannel.image=dimg

def rotate ():
    global img
    img=img.rotate(44)
    displayimage(img)

def flip1 ():
    global img
    img=img.transpose(Image.FLIP_LEFT_RIGHT)
    displayimage(img)

def flip2 ():
    global img
    img=img.transpose(Image.FLIP_TOP_BOTTOM)
    displayimage(img)

def openimg ():
    global img
    f=filedialog.askopenfilename(title="open")
    if f:
        img=Image.open(f)
        img=img.resize((600,600))
        displayimage(img)

    else:
        messagebox.showinfo("warning","no image is opened")

def save ():
    global img
    f=filedialog.asksaveasfile(title="save",defaultextension=".jpg")
    if f:
        img.save(f)
    else:
        messagebox.showinfo("warning","image is not saved")

b1=Button(win,text="rotate",command=rotate,width=25)
b1.grid(row=1,column=1)

b2=Button(win,text="flip 1",command=flip1,width=25)
b2.grid(row=2,column=1)

b3=Button(win,text="flip 2",command=flip2,width=25)
b3.grid(row=3,column=1)

b4=Button(win,text="open image",command=openimg,width=25)
b4.grid(row=0,column=1)

b5=Button(win,text="save",command=save,width=25)
b5.grid(row=4,column=1)

pannel=Label(win,bg="black")
pannel.grid(row=0,column=0,rowspan=12,padx=50,pady=50)
displayimage(img)

def greyscale ():
    global img
    img=img.convert("L")
    displayimage(img)

def invert ():
    global img
    img=ImageOps.invert(img)
    displayimage(img)

def brightness ():
    global img
    enhancer=ImageEnhance.Brightness(img)
    img=enhancer.enhance(2)
    displayimage(img)

def contrast ():
    global img
    enhancer=ImageEnhance.Contrast(img)
    img=enhancer.enhance(2)
    displayimage(img)


def sharpness ():
    global img
    enhancer=ImageEnhance.Sharpness(img)
    img=enhancer.enhance(2)
    displayimage(img)

b6=Button(win,text="Greyscale",command=greyscale,width=25)
b6.grid(row=5,column=1)

b7=Button(win,text="Invert",command=invert,width=25)
b7.grid(row=6,column=1)

b8=Button(win,text="Brightness",command=brightness,width=25)
b8.grid(row=7,column=1)

b9=Button(win,text="Contrast",command=contrast,width=25)
b9.grid(row=8,column=1)

b10=Button(win,text="sharpness",command=sharpness,width=25)
b10.grid(row=9,column=1)

win.mainloop()
