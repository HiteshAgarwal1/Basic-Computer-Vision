import numpy as np
import cv2 as cv
img=np.zeros((500,500,3), dtype='uint8')
font=cv.FONT_HERSHEY_PLAIN
cv.putText(img,"CV Course",(0,100),font,5,(123,38,78),4, cv.LINE_AA)
cv.imshow('bg',img)
cv.waitKey(0)
cv.destroyAllWindows()