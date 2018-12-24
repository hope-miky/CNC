import cv2
import numpy as np


ma = cv2.imread("pic2.png",0)
ma = cv2.resize(ma,(600,600))
#blured = cv2.pyrMeanShiftFiltering(ma,31,91)
#ma2 = cv2.Canny(blured,10,200)
cv2.destroyAllWindows()

_,cont,_ = cv2.findContours(ma,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
#cv2.drawContours(ma,cont,-1,(255,255,255),1)
#_, tresh = cv2.threshold(ma3,25,255,cv2.THRESH_BINARY_INV)
obj = np.zeros([ma.shape[0], ma.shape[1], 3])

for c in cont:
    #cv2.drawContours(obj,[c],-1,(255,255,255),0)
    d = c.tolist()
    for e in d:
        for f,g in e:
            print(f,g)
            obj[g][f]=255
            cv2.waitKey(30)
            cv2.imshow("finall",obj)
            
    #print(d)
    #print(c)
    area = cv2.contourArea(c)
    perim = cv2.arcLength(c,True)
    M = cv2.moments(c)
    #cx = int(M['m10']/M['m00'])
    #cy = int(M['m01']/M['m00'])
    #print(c)

    #cv2.circle(ma, (cx,cy),4, (0,0,255),-1)
    #print("A={}  P={}".format(area,perim))
    cv2.imshow("finall",obj)
    
    
cv2.imshow("finall",obj)
#cv2.imshow("fina7l",ma)








    
    


