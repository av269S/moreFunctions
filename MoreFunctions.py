#Import Modules

import tkinter
import datetime
import time
import random
import turtle
import cv2 
import cvlib as cv
from cvlib.object_detection import draw_bbox
from IPython.display import Image
from tkinter import *
from PIL import ImageTk,Image,ImageOps,ImageEnhance
from tkinter import filedialog
from tkinter import messagebox

#State Variables

F1 = 0
F2 = 0
Fnext = 0
n = 0
t = 1

#Functions

def calcAvgDep(Values):
    Avg = 0
    for i in Values:
        Avg = Avg + i

    Avg = Avg / len(Values)
    return Avg

def calcForce2ndLawOfMotionDep(Mass, Acceleration):
    return Mass * Acceleration

def calcAcceleration2ndLawOfMotionDep(Mass, Force):
    return Force / Mass

def calcMass2ndLawOfMotionDep(Acceleration, Force):
    return Force / Acceleration

def calcSpeedDep(Time, Distance):
    return Distance / Time

def calcTimeDep(Distance, Speed):
    return Distance / Speed

def calcDistanceDep(Speed, Time):
    return Speed * Time

def mileToKMDep(Input):
    return "Approx. result:", Input * 1.609


#Independant Function
def fibonacciSeqInd(n):
    F1 = 1
    F2 = 1
    print("These are the first", n, "terms of the fibonnaci sequence")
    print(F1)
    for j in range(t, n):
        print(F2)
        Fnext = F1 + F2
        F1 = F2
        F2 = Fnext

def calculatorDep(Num1, Num2, OP):
    int(Num1)
    int(Num2)
    if OP == "+" :
        return Num1 + Num2
    elif OP == "-":
        return Num1 - Num2
    elif OP == "/":
        return Num1 / Num2
    elif OP == "*":
        return Num1 * Num2
    else:
        return "Invalid Input"

#def abbrevation(Phrases):
 #   return Phrases[0]
  #  for i in Phrases:
   #     if i == " ":
    #        return i + 1
    
def classify(img):
    path=("moreFunction/object classifier/")
    image=cv2.imread(path+img)
    bbox,label,conf=cv.detect_common_objects(image,model="yolov3")
    print(bbox,label,conf)
    output=draw_bbox(image,bbox,label,conf)
    cv2.imwrite(path+"object detected.jpg",output)
    display(Image(filename=path+"object detected.jpg"))




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





                               
