import cv2 as cv

people=['diane','kriti','lea','sophie']
haar_cascade=cv.CascadeClassifier('haar_face.xml')
face_recognizer=cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')
img=cv.imread(r'C:\Users\anshu\Downloads\opencv\test\diane\d.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

faces_rect=haar_cascade.detectMultiScale(gray,1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi=gray[y:y+h,x:x+w]
    label,confidence=face_recognizer.predict(faces_roi)
    print(people[label])
    print(confidence)
    cv.putText(img,str(people[label]),(25,25),cv.FONT_HERSHEY_COMPLEX,1.0,(0,0,255),2)
    cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv.imshow('Detected',img)
cv.waitKey(0)