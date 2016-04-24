from cv2 import * #Import functions from OpenCV
import cv2
import numpy as np
import Image


e1 = cv2.getTickCount()
source = cv2.imread("games.jpg")
final = cv2.medianBlur(source, 3)
   
cv2.imshow('Source_Picture', source) #Show the image
cv2.imshow('Median Filtered Image', final) #Show the image
cv2.waitKey()
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)


kernel_size = 3
scale = 1
delta = 0
ddepth = cv2.CV_16S

img = cv2.imread('games.jpg')
img = cv2.GaussianBlur(img,(3,3),0)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray_lap = cv2.Laplacian(gray,ddepth,ksize = kernel_size,scale = scale,delta = delta)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow('Marr-Hildreth algorithm image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

def normalize(arr):
    """
    Linear normalization
    http://en.wikipedia.org/wiki/Normalization_%28image_processing%29
    """
    # Do not touch the alpha channel
    for i in range(3):
        minval = arr[...,i].min()
        maxval = arr[...,i].max()
        if minval != maxval:
            arr[...,i] -= minval
            arr[...,i] *= (255.0/(maxval-minval))
    return arr

img = Image.open('games.jpg').convert('RGBA')
a = np.array(img)
b = normalize(a)

im = Image.fromarray(b)
im.save('output.jpg')
