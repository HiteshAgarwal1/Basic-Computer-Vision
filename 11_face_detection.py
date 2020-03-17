import cv2 as cv
#https://github.com/opencv/opencv/blob/master/data/haarcascades
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
videoCapture=cv.VideoCapture(0)
#or from pic.. read the pic instead of video
scale_factor=1.3
while 1:
    ret, pic = videoCapture.read() #comment the line for face detectiion in the pic
    faces = face_cascade.detectMultiScale(pic, scale_factor, 5)

    for(x,y,w,h) in faces:
        cv.rectangle(pic,(x,y),(x+w,y+h),(255,0,0),2)
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(pic,'Me',(x,y),font,1,(0,255,0),2,cv.LINE_AA)
    
    cv.imshow('Camera',pic)
    if cv.waitKey(5) & 0xFF==ord('q'):
        break
cv.destroyAllWindows()
