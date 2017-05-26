import cv2
import numpy as np

cap=cv2.VideoCapture(0)
template=cv2.imread("e.jpg",0)
w,h=template.shape[::-1]
while True:
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    res=cv2.matchTemplate(gray,template,cv2.TM_CCOEFF_NORMED)
    threshold=0.60
    loc=np.where(res>=threshold)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame,pt,(pt[0]+w,pt[1]+h),(0,255,255),2)

    cv2.imshow("detected",frame)




    if cv2.waitKey(1) & 0xFF==ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
