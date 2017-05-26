import cv2
import numpy as np
select=False
def mouse_callback(event,x,y,flags,params):
    global select,frame,template,w,h,gray
    if event == cv2.EVENT_LBUTTONDOWN:
        select=False
        template=gray[x:(x+40),y:(y+40)]
        w,h=template.shape[::-1]
        print template.shape
        select=True
global gray
cv2.namedWindow('detected')
cv2.setMouseCallback('detected',mouse_callback)

cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if select==True:
        res=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
        threshold=0.95
        loc=np.where(res>=threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

    cv2.imshow('detected',frame)




    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
