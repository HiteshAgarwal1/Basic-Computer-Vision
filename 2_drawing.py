import numpy as np
import cv2 as cv
img=np.zeros((500,500,3), dtype='uint8')
cv.circle(img,(22,33),15,(21,76,123),thickness=3,lineType=8,shift=0)
cv.imshow('bg',img)
cv.waitKey(0)
cv.destroyAllWindows()