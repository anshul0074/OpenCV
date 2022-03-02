import cv2 as cv
import numpy as np

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
blank=np.zeros(img.shape,dtype='uint8')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# blur=cv.GaussianBlur(gray,(7,7),cv.BORDER_DEFAULT)
# canny=cv.Canny(blur,threshold1=125,threshold2=175)
# cv.imshow('Canny',canny)
ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
contour, hierarchy=cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contour))
drawcontours=cv.drawContours(blank,contour,-1,color=(255,0,0),thickness=1)
#for getting all contours specify third argument=-1
cv.imshow('Contours',drawcontours)
cv.waitKey(0)