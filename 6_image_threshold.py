import numpy as np
import cv2 as cv
# For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0,
# otherwise it is set to a maximum value. The function cv.threshold is used to apply the thresholding.
# The first argument is the source image, which should be a grayscale image.

img=cv.imread('hor.png',0)
thres_value=200
(T_value,binary_hold)=cv.threshold(img,thres_value,255,cv.THRESH_BINARY)
cv.imshow('pic',binary_hold)
cv.waitKey()
cv.destroyAllWindows()