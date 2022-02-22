import cv2 as cv

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#simple thresholding ; arguments->(source_image,threshold_value,max_value,threshold_type)
thresh_val,thresh_img=cv.threshold(gray,100,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold',thresh_img)
print(thresh_val)

#adaptive thresholding ; arguments->(source_image,max_value,threshold_method,threshold_type,kernal_size,C_value)
adaptive_threshold_img=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,19,9)
cv.imshow('Adaptive threshold',adaptive_threshold_img)

cv.waitKey(0)