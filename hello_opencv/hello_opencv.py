import cv2
import numpy

img=cv2.imread("/home/jkachhadia/LearningOpencv/hello_opencv/frank.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("frankgray.png",img)
