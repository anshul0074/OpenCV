import cv2 as cv
import numpy as np

img=cv.imread('photos/anshul.jpg')
cv.imshow('original',img)

#flipping image
# 0->vertical flip ; 1->horizontal flip ; -1->both combined
flipped=cv.flip(img,-1)
cv.imshow('Flipped',flipped)

#translation of image
def translate(img,x,y):
    dimensions=(img.shape[1],img.shape[0])
    transmat=np.float32([[1,0,x],[0,1,y]])
    return cv.warpAffine(img,transmat,dimensions)

translated=translate(img,-100,200)
cv.imshow('Translated',translated)

#rotation of image
def rotate(img,angle,refpoint=None):
    height=img.shape[0]
    width=img.shape[1]
    dimensions=(width,height)
    if(refpoint==None):
        refpoint=(width//2,height//2)
    rotmat=cv.getRotationMatrix2D(refpoint,angle,scale=1.0)
    return cv.warpAffine(img,rotmat,dimensions)
# +ve angle ->anticlockwise rotation ; -ve angle ->clockwise rotation
rotated=rotate(img,-30)
cv.imshow('Rotated',rotated)

cv.waitKey(0)