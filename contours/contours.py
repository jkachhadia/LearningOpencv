import cv2
import numpy as np

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    ret, thresh=cv2.threshold(gray,127,255,0)
    _,contours, hierarchy= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
    cv2.imshow('contours',frame)
    if cv2.waitKey(1) & 0xFF==ord("q"):
        break
cv2.destroyAllWindows()
