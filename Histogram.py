import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(r"/home/rpi/Desktop/Sneh/download.jpeg")
#rescaling and resizing
def rescaleImg(img,scale = 0.5):
    width = int(img.shape[1] * scale)
    height = int(img.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(img,dimensions,interpolation=cv.INTER_AREA)

resized_image1 = rescaleImg(img)
cv.imshow('My Photos',resized_image1)

#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
resized_image2 = rescaleImg(gray)
cv.imshow('Gray',resized_image2)

#GrayScale Histogram

gray_hist = cv.calcHist([resized_image2],[0],None,[256],[0,256])
plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('No. of pixels ')
plt.plot(gray_hist)
plt.xlim([0,256])

#You can also apply mask in place of None

#Color histogram

colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([resized_image1],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()    


cv.waitKey(0)