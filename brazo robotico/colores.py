import cv2
import numpy as np

cap = cv2.VideoCapture(0)

"""redbajo1=np.array([0,100,20],np.uint8)
redalto1=np.array([8,2555,255],np.uint8) 

redbajo2=np.array([175,100,20],np.uint8)
redalto2=np.array([179,255,255],np.uint8)


while True:
    ret,frame = cap.read()
    if ret==True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        maskred1= cv2.inRange(frameHSV, redbajo1, redalto1)
        maskred2 = cv2.inRange(frameHSV, redbajo2, redalto2)
        maskred = cv2.add(maskred1, maskred2)
        maskredvis = cv2.bitwise_and(frame, frame, mask=maskred)
        cv2.imshow('maskredvis',maskredvis)
        cv2.imshow('maskred',maskred)
        cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xFF == ord('s'):
             break"""   

azulbajo = np.array([100,100,20],np.uint8)
azulalto = np.array([125,255,255],np.uint8)

while True:
    ret, frame = cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV, azulbajo, azulalto)
        contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
       #cv2.drawContours(frame, contornos, -1, (255,0,0), 3)
        for c in contornos:
            area = cv2.contourArea(c)
            if area > 3000:
                m=cv2.moments(c)
                if (m["m00"]==0): m["m00"]=1
                x=int(m["m10"]/m["m00"])
                y=int(m["m01"]/m["m00"])
                cv2.circle(frame, (x, y), 7, (0,255,0), -1)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, '{},{}'.format(x,y), (x+10,y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
                nuevoContorno = cv2.convexHull(c)
                cv2.drawContours(frame, [c], 0, (255,0,0), 3)
       #cv2.imshow('maskazul',mask)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()

