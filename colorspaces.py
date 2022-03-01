import cv2 as cv
import matplotlib.pyplot as plt

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
# plt.imshow(img)
# plt.show()

#BGR to Gray
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#BGR to HSV
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#BGR to L*a*b
lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

#BGR to RGB
rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('RGB',rgb)
# plt.imshow(rgb)
# plt.show()

#HSV to BGR
hsv_bgr=cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('HSV_BGR',hsv_bgr)
cv.waitKey(0)