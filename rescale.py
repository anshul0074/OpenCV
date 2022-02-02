import cv2 as cv

def rescale_frame(frame,scale=0.25):
    height=int(frame.shape[0]*scale)
    width=int(frame.shape[1]*scale)
    return cv.resize(frame,(width,height),interpolation=cv.INTER_AREA)
#for images
img = cv.imread('photos/coin.jpg')
cv.imshow('coin',img)
new_img=rescale_frame(img)
cv.imshow('new_image',new_img)
cv.waitKey(0)

#for videos
#capture = cv.VideoCapture('videos/nobody.mkv')
#while 1:
#    istrue, frame = capture.read()
#    new_frame=rescale_frame(frame)

#    #cv.imshow('video',frame)
#    cv.imshow('new_video',new_frame)
#    if(cv.waitKey(20) and 0xFF== ord('d')):
#        break
#capture.release()
#cv.destroyAllWindows()