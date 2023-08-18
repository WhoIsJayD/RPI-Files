import cv2 as cv

cam = cv.VideoCapture(0)

#rescaling and resizing
def rescaleFrame(frame,scale = 0.7):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame,dimensions)


while True :
    isTrue , frame = cam.read()
    frame_resized = rescaleFrame(frame)

    #cv.imshow('Video',frame)
    cv.imshow('Video Resized ', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cam.release()
cv.destroyAllWindows()

cv.waitKey(0)