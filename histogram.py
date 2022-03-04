import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
blank=np.zeros(img.shape[:2],dtype='uint8')

# #histogram for grayscale (without mask)
# gray_hist=cv.calcHist([gray],[0],None,[256],[0,256]) #arguments-> (images,channels,mask,histSize (bins) ,range)
# plt.figure()
# plt.title('Grayscale histogram without mask')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()

# #histogram for grayscale (with mask)
# cir=cv.circle(blank,center=(img.shape[1]//2,img.shape[0]//2-200),radius=150,color=255,thickness=-1)
# mask=cv.bitwise_and(gray,gray,mask=cir)
# cv.imshow('Mask',mask)
# gray_mask_hist=cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Grayscale histogram with mask')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.xlim([0,256])
# plt.plot(gray_mask_hist)
# plt.show()

# #histogram for BGR image without mask
# color= ('b','g','r')
# plt.figure()
# plt.title('BGR histogram without mask')
# plt.xlabel('Bins')
# plt.ylabel('Number of pixels')
# plt.xlim([0,256])
# for i,col in enumerate(color):
#     hist=cv.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(hist,col)
# plt.show()

#histogram for BGR image with mask
color= ('b','g','r')
cir=cv.circle(blank,center=(img.shape[1]//2,img.shape[0]//2-200),radius=150,color=255,thickness=-1)
mask=cv.bitwise_and(img,img,mask=cir)
cv.imshow('Mask',mask)
plt.figure()
plt.title('BGR histogram with mask')
plt.xlabel('Bins')
plt.ylabel('Number of pixels')
plt.xlim([0,256])
for i,col in enumerate(color):
    hist=cv.calcHist([img],[i],cir,[256],[0,256])
    plt.plot(hist,col)
plt.show()

cv.waitKey(0)