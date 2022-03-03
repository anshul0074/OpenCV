import cv2 as cv
import numpy as np

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#canny method
canny=cv.Canny(gray,threshold1=125,threshold2=175)
cv.imshow('Canny',canny)

#laplace method ; arguments->(source_image,data_depth)
laplace=cv.Laplacian(gray,cv.CV_64F)
laplace=np.uint8(np.absolute(laplace))
cv.imshow('Laplace',laplace)

#sobel method ; arguments-> (source_image,data_depth,dx,dy)
x_sobel=cv.Sobel(gray,cv.CV_64F,1,0)
y_sobel=cv.Sobel(gray,cv.CV_64F,0,1)
combined_sobel=cv.bitwise_or(x_sobel,y_sobel)
cv.imshow('Sobel',combined_sobel)

cv.waitKey(0)