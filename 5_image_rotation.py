import numpy as np
import cv2 as cv
img=cv.imread('hor.png')
col=img.shape[1]
row=img.shape[0]
centre=(col/3,row/3)
angle=-90
M = cv.getRotationMatrix2D(centre,angle,0.5)
rotated=cv.warpAffine(img,M,(col,row))
cv.imshow('origional',rotated)
cv.waitKey(0)
cv.destroyAllWindows()