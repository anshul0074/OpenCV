import cv2 as cv
import numpy as np

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
#splitting
b,g,r=cv.split(img)
# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

#merging
blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
merged=cv.merge([b,g,r])
cv.imshow('Merged',merged)

cv.waitKey(0)