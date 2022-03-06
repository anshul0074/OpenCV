import cv2 as cv
import numpy as np

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
blank=np.zeros(img.shape[:2],dtype='uint8')
cir=cv.circle(blank,center=(img.shape[1]//2,img.shape[0]//2-200),radius=150,color=255,thickness=-1)
cv.imshow('Mask',cir)
masked=cv.bitwise_and(img,img,mask=cir)
cv.imshow('Masked',masked)

cv.waitKey(0)