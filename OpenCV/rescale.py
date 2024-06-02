import cv2 as cv


# Read image
img= cv.imread('image/my.jpg')
cv.imshow('Avadhesh',img)


def resize(frame,scale):
        # Work for image,video and live video
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimension=(width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)


newimg=resize(img,0.5)
cv.imshow('Avadhesh_resized',newimg)
cv.imwrite('image/resized_my.jpg',newimg)  # save image
cv.waitKey(0)

# Read video
capture= cv.VideoCapture(0)

def change_resolution(capture,width,height):     
    # Resize work for live video only
    # Resize capture to width,height
    capture.set(3,width)
    capture.set(4,height)
    return capture

change_resolution(capture,30,30)

while True:
    isImg,frame=capture.read()
    cv.imshow('Live video',frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()