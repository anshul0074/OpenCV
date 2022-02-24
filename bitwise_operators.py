import cv2 as cv
import numpy as np

blank=np.zeros(shape=(500,500),dtype='uint8')


rec=cv.rectangle(blank.copy(),pt1=(40,40),pt2=(400,400),color=255,thickness=-1)
cv.imshow('Rectangle',rec)
cir=cv.circle(blank.copy(),center=(250,250),radius=200,color=255,thickness=-1)
cv.imshow('Circle',cir)

#AND -> intersection
And=cv.bitwise_and(rec,cir)
cv.imshow('AND',And)

#OR -> Union
Or=cv.bitwise_or(rec,cir)
cv.imshow('OR',Or)

#XOR -> (OR - AND)
Xor=cv.bitwise_xor(rec,cir)
cv.imshow('XOR',Xor)

#NOT -> flips pixels
Not=cv.bitwise_not(cir)
cv.imshow('NOT',Not)

cv.waitKey(0)