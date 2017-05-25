import cv2
import numpy as np

img1=cv2.imread("bangkok.jpg")
img2=cv2.imread("newyork.jpg")

add=img1+img2
cv2.imshow("add",add)

add1=cv2.add(img1,img2)
cv2.imshow("add1",add1)

weighted=cv2.addWeighted(img1,0.6,img2,0.4,0)
cv2.imshow("weighted",weighted)

img3=cv2.imread("python.png")
rows, cols, channels = img3.shape
roi = img1[0:rows,0:cols]

img2gray=cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask= cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("mask",mask)
mask_inv=cv2.bitwise_not(mask)

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
img3_fg=cv2.bitwise_and(img3,img3,mask=mask)
cv2.imshow("img1bg",img1_bg)

dst= cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols]=dst
cv2.imshow("img1final",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
