import cv2 as cv

img=cv.imread('photos/anshul.jpg')
cv.imshow('Original',img)
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)
haar_cascade=cv.CascadeClassifier('haar_face.xml')
rectangle_faces=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)
print(len(rectangle_faces))
for (x,y,w,h) in rectangle_faces:
    cv.rectangle(img,pt1=(x,y),pt2=(x+w,y+h),color=(0,0,255),thickness=2)
cv.imshow('Detected',img)

cv.waitKey(0)