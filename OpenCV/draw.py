import cv2 as cv
import numpy as np

# Blank image
blank=np.zeros((500,500,3),dtype='uint8')
cv.imshow('blank',blank)

# Green image
blank[:]=0,255,0
cv.imshow('Green',blank)

# Green Area
blank[:]=0,0,0
blank[100:200,200:300]=0,255,0
cv.imshow('Semi_Green',blank)

# Rectangle Border
blank[:]=0,0,0
cv.rectangle(blank,(0,0),(200,200),(0,255,0),2)
cv.imshow('Rectangle Border',blank)

# Filled Rectangle
# Rectangle Border
blank[:]=0,0,0
# cv.rectangle(blank,(0,0),(200,200),(0,255,0),thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(200,200),(0,255,0),thickness=-1)
cv.imshow('Filled Rectangle Border',blank)


# For circle =>  cv.circle(....)
# For line   =>  cv.line(......)


# For Text
cv.putText(blank,"Avadhesh",(0,200),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,255),3)
cv.imshow('Text',blank)
cv.waitKey(0)