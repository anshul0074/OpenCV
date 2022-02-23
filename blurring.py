import cv2 as cv

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img) 

#Average blur
avg=cv.blur(img,ksize=(5,5))
cv.imshow('Average',avg)

#Gaussian blur 
gauss=cv.GaussianBlur(img,ksize=(5,5),sigmaX=0)
cv.imshow('Gaussian',gauss)

#Median blur ; ksize should be integer, not tuple
med=cv.medianBlur(img,ksize=5)
cv.imshow('Median',med)

#Bilateral blur ; retains edges ; arguments-> (source_image,diameter,sigmaColor,sigmaSpace)
btrl=cv.bilateralFilter(img,5,15,35)
cv.imshow('Bilateral',btrl)

cv.waitKey(0)