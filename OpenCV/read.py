import cv2 as cv


# Read image
img= cv.imread('image/my.jpg')
cv.imshow('Avadhesh',img)
print(img.shape[1])  #shape[0] is height and shape[1] is width
cv.waitKey(0)

# Read video
capture= cv.VideoCapture(0)
while True:
    isImg,frame=capture.read()
    cv.imshow('Live video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()