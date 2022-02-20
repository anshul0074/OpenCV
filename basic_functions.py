import cv2 as cv

img=cv.imread('photos/anshul.jpg')
cv.imshow('original',img)

#resize image ; arguments->(source_image,new_image_size,interpolation)
#shrinking->INTER_AREA
#enlarging->INTER_LINEAR or INTER_CUBIC
resized=cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)

#crop image
cropped=img[100:200,200:400]
#cv.imshow("Cropped",cropped)

#convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#Blur image ; arguments-> (source_image,kernal_size,cv.BORDER_DEFAULT) ; 
# kernal_size should be odd
blur=cv.blur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

#detect edge
canny=cv.Canny(blur,threshold1=100,threshold2=150)
#cv.imshow('Canny',canny)

#dilate image ; arguments-> (source_image,kernal_size,iterations);
dilated=cv.dilate(canny,(7,7),iterations=3)
#cv.imshow('Dilated',dilated)

#eroding image (got back canny after applying to dilated)
eroded=cv.erode(dilated,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

cv.waitKey(0)