import numpy as np
import cv2 as cv
img=cv.imread('hor.png')
col=img.shape[1]
row=img.shape[0]
bg=np.float32([[1,0,30],[0,1,70]])
shifted=cv.warpAffine(img,bg,(col,row))
cv.imshow('origional',shifted)
cv.waitKey(0)
cv.destroyAllWindows()