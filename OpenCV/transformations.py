import cv2 as cv
import numpy as np

img=cv.imread('image/resized_my.jpg')
cv.imshow('image',img)

# Translation
def translate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions=(img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(img,200,300)
cv.imshow('translated',translated)

# Rotation
def rotate(img,angle,rotatePT=None):
    (height,width)=img.shape[:2]
    if rotatePT is None :
        rotatePT=(width//2,height//2)
    RotMat=cv.getRotationMatrix2D(rotatePT,angle,1.0)
    dimensions=(width,height)
    return cv.warpAffine(img,RotMat,dimensions)

rotated=rotate(img,45)
cv.imshow('rotated',rotated)


# Flip
flip = cv.flip(img,0)
cv.imshow('flip',flip)
# 0 x-axis flip
# 1 y-axis flip
# -1 both x,y axis



cv.waitKey(0)
