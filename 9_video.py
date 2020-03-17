import numpy as np
import cv2 as cv
cap=cv.VideoCapture('vid.mp4')
while(cap.isOpened()):
    rect, frame = cap.read()
    cv.imshow('vid',frame)
    if cv.waitKey(1) and 0xFF == ord('q'):
        break
cap.release()
cv.destroyAllWindows()