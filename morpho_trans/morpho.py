import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red=np.array([0,100,0])
    upper_red=np.array([15,255,255]) #HSV range for my face extraction! Your can be different :p

    mask=cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((10,10),np.uint8)
    erosion=cv2.erode(mask,kernel,iterations=1)
    dilation=cv2.dilate(mask,kernel, iterations=1)

    opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
    closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)


    cv2.imshow("erosion",erosion)
    cv2.imshow("dilation",dilation)
    cv2.imshow("original",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("res",res)
    cv2.imshow("opening",opening)
    cv2.imshow("closing",closing)

    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
