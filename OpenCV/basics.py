import cv2 as cv

img=cv.imread('image/my.jpg')
cv.imshow('RGB',img)

# Converting to Grayscale
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# Blur
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade (boundaries)
canny=cv.Canny(img,55,55)
cv.imshow('Canny',canny)

# Dilate the image
dilated= cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilated)

# Erode the image
eroded=cv.erode(dilated,(3,3),5)
cv.imshow('Eroded',eroded)

# Resize
resized=cv.resize(img,(400,400),interpolation=cv.INTER_AREA)
cv.imshow('resized',resized)

# Cropped
cropped=img[20:200,100:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)