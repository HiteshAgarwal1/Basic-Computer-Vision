import numpy as np
import cv2 as cv
img=cv.imread('hor.png',20)

thres1=0
thres2=50
edged=cv.Canny(img,thres1,thres2)
cv.imshow('edge',edged)
cv.waitKey()
cv.destroyAllWindows()