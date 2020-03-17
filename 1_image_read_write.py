import cv2 as cv
img=cv.imread('hor.png',15)
cv.imwrite('origional.jpg',img)
cv.imshow('origional',img)
cv.waitKey(0)
cv.destroyAllWindows()
