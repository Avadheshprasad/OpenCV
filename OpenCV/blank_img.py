import cv2 as cv
import numpy as np

# 400*500
blank=np.zeros((500,400),dtype='uint8')
cv.imshow('blank',blank)
cv.imwrite('image/blank.jpg',blank)
cv.waitKey(0)