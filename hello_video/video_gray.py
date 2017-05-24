import cv2
import numpy
size=(640,480)
cap= cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter('output.avi', fourcc, 20.0,size )
while True:
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("frame",frame)
    cv2.imshow("gray frame",gray)
    a=gray.resize(size)
    out.write(a)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
