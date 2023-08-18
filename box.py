import cv2
import numpy as np

framewidth=640
frameheight=480
cap=cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)


def empty():
    pass

cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters",640,240)
cv2.createTrackbar("Threshold1","Parameters",23,255,empty)
cv2.createTrackbar("Threshold2","Parameters",197,255,empty)

def getContour(img,imgContour):
    
    contours, hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>1000:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if len(approx)==4:
                cv2.drawContours(imgContour,cnt,-1, (255,0,255),7)
                x,y,w,h=cv2.boundingRect(approx)
                cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),5)
                cv2.putText(imgContour,'Box',(x+w+20,y+20), cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)
                for i in contours:
                    M=cv2.moments(i)
                    if M['m00']!=0:
                        cx=int(M['m10']/M['m00'])
                        cy=int(M['m01']/M['m00'])
                        cv2.circle(imgContour,(cx,cy),7,(0,0,255),-1)
                        cv2.putText(imgContour,'center',(cx-20,cy-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)
                        print(f"x:{cx} y: {cy}")
                        
while True:
    success, img=cap.read()
    imgContour= img.copy()
    
    imgBlur=cv2.GaussianBlur(img,(7,7),1)
    imgGray=cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    
    threshold1=cv2.getTrackbarPos("Threshold1","Parameters")
    threshold2=cv2.getTrackbarPos("Threshold2","Parameters")
    imgCanny=cv2.Canny(imgGray,threshold1,threshold2)
    kernel=np.ones((5,5))
    imgDil=cv2.dilate(imgCanny,kernel,iterations=1)
    
    getContour(imgDil,imgContour)
    
    cv2.imshow("Result",imgContour)
    if cv2.waitKey(2) & 0xFF== ord('q'):
        break
    