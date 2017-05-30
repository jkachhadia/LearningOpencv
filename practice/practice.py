import cv2
import numpy as np
import pickle
from sklearn.neural_network import MLPClassifier
clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
                    hidden_layer_sizes=(5, 2), random_state=1)

def mouse_callback(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print classified[y,x]
        select=True

classified=cv2.imread("blr_class.tif",-1)
in3=cv2.imread("blr_3.tif",0)
in4=cv2.imread("blr_4.tif",0)
in5=cv2.imread("blr_5.tif",0)
limit=[2051,2032]
final= np.zeros([limit[0], limit[1], 4], dtype=np.uint8)
inp=np.zeros([limit[0]*limit[1], 4], dtype=np.uint8)
out=np.zeros([limit[0]*limit[1], 4], dtype=np.uint8)
for a in range(0,limit[0]):
    for b in range(0,limit[1]):
        final[a,b]=[in3[a,b],in4[a,b],in5[a,b],255]
print "created 3-d array"
c=0
for a in range(0,limit[0]):
    for b in range(0,limit[1]):
        inp[c]=final[a,b]
        out[c]=classified[a,b]
        c=c+1
print "converted to 2-d array"
cv2.namedWindow('classified')
cv2.setMouseCallback('classified',mouse_callback)
c=0
output=np.zeros([limit[0]*limit[1], 1], dtype=np.uint8)
for a in out:
    if np.all(a==[156,247,255,255]):
        output[c]=4
        c=c+1
    elif np.all(a==[120,227,129,255]):
        output[c]=2
        c=c+1
    elif np.all(a==[0,0,255,255]):
        output[c]=1
        c=c+1
    elif np.all(a==[255,141,85,255]):
        output[c]=3
        c=c+1
    else:
        output[c]=0
        c=c+1

print "made output categorical"

print output[0], output[1]

# cv2.imshow("final",final)
# cv2.imshow("classified",classified)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



clf.fit(inp, output)
with open("clf.pickle",'wb') as f:
    pickle.dump(clf,f)
    print "done"

print clf.predict([inp[0],inp[1]])
