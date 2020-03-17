import numpy as np
import cv2 as cv
img=cv.imread('hor.png',20)

matrix=(7,7)
gaussianBlurred=cv.GaussianBlur(img,matrix,0)

kernal_value=7
medianBlurred=cv.medianBlur(img,kernal_value)

dimpxl=15
color=80
space=100
bilateralFilter=cv.bilateralFilter(img,dimpxl,color,space)

cv.imshow('origional',img)
cv.imshow('gaussianBlurred',gaussianBlurred)
cv.imshow('medianBlurred',medianBlurred)
cv.imshow('bilateralFilter',bilateralFilter)
cv.waitKey()
cv.destroyAllWindows()