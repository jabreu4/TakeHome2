from easygui import *
import sys
from cv2 import * #Import functions from OpenCV
import cv2
import numpy as np
import Image

msgbox("Welcome to Exam #2 Take Home. Click Ok to enter the image to be processed")
imagePath = fileopenbox()

time = 0
msg ="What image processing algorithm you want to  work with?"
title = "Image Processing Algorithms"
choices = ["MedianFilter", "WeinerFilter", "MarrHildrethEdgeDetector"]
choice = choicebox(msg, title, choices)

numberThreads = integerbox(msg="What is the number of threads you want to work with"
                  , title = "Number Of Threads"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 200)

numberCores = integerbox(msg="What is the number of cores you want to work with"
                  , title = "Number Of Cores"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 300)

numberThreadsPerCore = integerbox(msg="What is the number of threads per core you want to work with"
                  , title = "Number Of Threads per Core"
                  , default = 0
                  , lowerbound = 0
                  , upperbound = 400)


def medianFilter():
    e1 = cv2.getTickCount()
    source = cv2.imread(imagePath)
    final = cv2.medianBlur(source, 9)
    e2 = cv2.getTickCount()
    time = (e2 - e1)/ cv2.getTickFrequency()
    msgbox(msg=time, title="Execution Time", ok_button="OK")
    cv2.imshow('Original Picture', source) #Show the image
    cv2.imshow('Median Filtered Image', final) #Show the image
    cv2.waitKey()
    cv2.destroyAllWindows()

def MarrHildrethEdgeDetector():
  e1 = cv2.getTickCount()
  kernel_size = 3
  scale = 1
  delta = 0
  ddepth = cv2.CV_16S
  source = cv2.imread(imagePath)
  img = cv2.imread(imagePath)
  img = cv2.GaussianBlur(img,(3,3),0)
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

  gray_lap = cv2.Laplacian(gray,ddepth,ksize = kernel_size,scale = scale,delta = delta)
  dst = cv2.convertScaleAbs(gray_lap)
  e2 = cv2.getTickCount()
  time = (e2 - e1)/ cv2.getTickFrequency()
  msgbox(msg=time, title="Execution Time", ok_button="OK")
  cv2.imshow('Original Picture', source) #Show the image
  cv2.imshow('Marr-Hildreth algorithm image',dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()
   


if choice == 'MedianFilter':
  medianFilter()
elif choice == 'MarrHildrethEdgeDetector':
  MarrHildrethEdgeDetector()




