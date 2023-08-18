import cv2
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("fuck you")
while True:
    ret,frame = cap.read()
    frame=cv2.resize(frame,None,fx=0.8,fy=0.8,interpolation=cv2.INTER_AREA)
    cv2.imshow("input",frame)
    
    c=cv2.waitKey(1)
    if c==27:
        break
cap.release()

    