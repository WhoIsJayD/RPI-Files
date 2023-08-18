import cv2 as cv

#rescaling and resizing
def rescaleFrame(frame,scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

img = cv.imread(r"/home/rpi/Desktop/Sneh/download.jpeg")
cv.imshow('Image',img)
cv.waitKey(0)