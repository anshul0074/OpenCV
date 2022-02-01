import cv2 as cv

#for images
#img = cv.imread('photos/coins.jpg')
#cv.imshow('coins',img)
#cv.waitKey(0)

#for videos
capture = cv.VideoCapture('videos/nobody.mkv')
while 1:
    istrue, frame = capture.read()
    cv.imshow('video',frame)
    if(cv.waitKey(20) and 0xFF== ord('k')):
        break
capture.release()
cv.destroyAllWindows()