import cv2 as cv
import numpy as np

blank=np.zeros(shape=(500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)

#fill colour fully
blank[:]=0,255,255
#cv.imshow('r+g=y',blank)
#fill colour partially
blank[100:200,200:300]=255,0,0
#cv.imshow('partial',blank)

#draw line
line=cv.line(blank,pt1=(0,0),pt2=(200,300),color=(0,255,0),thickness=2)
#cv.imshow('line',line)

#draw rectangle
rec=cv.rectangle(blank,pt1=(0,0),pt2=(blank.shape[1]//2,blank.shape[0]//2),color=(255,0,0),thickness=2)
#cv.imshow('rectangle',rec)

#draw circle
cir=cv.circle(blank,center=(200,200),radius=51,color=(0,0,255),thickness=2)
#cv.imshow('circle',cir)

#write text ; arguments->(source_image,text,starting_coordinates,fontface,fontscale,color,thickness)
txt=cv.putText(blank,'I am batman',(50,225),cv.FONT_HERSHEY_COMPLEX,1.5,color=(0,0,250),thickness=2)
cv.imshow("text",txt)
cv.waitKey(0)