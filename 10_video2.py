import numpy as np
import cv2 as cv
cap=cv.VideoCapture('vid.mp4')
fourcc=cv.VideoWriter_fourcc(*'XVID')
fps=30
frame=(720,480)
out=cv.VideoWriter('sample.avi',fourcc,fps,frame)
while(cap.isOpened()):
    rect, frame = cap.read()
    cv.imshow('vid',frame)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break
out.release()
cap.release()
cv.destroyAllWindows()