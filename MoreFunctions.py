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
    
def encrypt(Phrase):
    str(Phrase)
    return Phrase.encode(encoding="UTF-8", errors="strict")

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
