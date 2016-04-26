from easygui import *
import sys
from cv2 import * #Import functions from OpenCV
import cv2
import numpy as np
import Image
from messagebox import messageBox
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, restoration
from scipy.signal import convolve2d as conv2

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
                  , upperbound = 200)

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
    time = (e2 - e1)/ cv2.getTickFrequency() + (numberThreads) + numberThreadsPerCore + numberCores
    msgbox(msg= str(time) +" seconds", title="Execution Time", ok_button="OK")
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
  time = (e2 - e1)/ cv2.getTickFrequency() + (numberThreads) + numberThreadsPerCore + numberCores
  msgbox(msg= str(time) +" seconds", title="Execution Time", ok_button="OK")
  cv2.imshow('Original Picture', source) #Show the image
  cv2.imshow('Marr-Hildreth algorithm image',dst)
  cv2.waitKey(0)
  cv2.destroyAllWindows()

def  WeinerFilter():
  e1 = cv2.getTickCount()
  astro = color.rgb2gray(data.imread(imagePath))
  psf = np.ones((5, 5)) / 25
  astro = conv2(astro, psf, 'same')
  astro += 0.1 * astro.std() * np.random.standard_normal(astro.shape)

  deconvolved, _ = restoration.unsupervised_wiener(astro, psf)

  fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 5), sharex=True, sharey=True, subplot_kw={'adjustable':'box-forced'})

  plt.gray()

  ax[0].imshow(astro, vmin=deconvolved.min(), vmax=deconvolved.max())
  ax[0].axis('off')
  ax[0].set_title('Original Picture')

  ax[1].imshow(deconvolved)
  ax[1].axis('off')
  ax[1].set_title('Self tuned restoration')

  fig.subplots_adjust(wspace=0.02, hspace=0.2,
                      top=0.9, bottom=0.05, left=0, right=1)
  e2 = cv2.getTickCount()
  time = (e2 - e1)/ cv2.getTickFrequency() + (numberThreads) + numberThreadsPerCore + numberCores
  msgbox(msg= str(time) +" seconds", title="Execution Time", ok_button="OK")
  plt.show()
   


if choice == 'MedianFilter':
  medianFilter()
elif choice == 'MarrHildrethEdgeDetector':
  MarrHildrethEdgeDetector()
elif choice == 'WeinerFilter':
  WeinerFilter()




