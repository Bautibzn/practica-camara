import cv2
import mediapipe as mp
import math

dispositivoCaputra = cv2.VideoCapture(0)
mpManos = mp.solutions.hands

manos = mpManos.Hands(static_image_mode = False, 
                      max_num_hands=1,
                      min_detection_confidence=0.9,
                      min_tracking_confidence=0.8)

mpDibujar = mp.solutions.drawing_utils
cambiar = 0
while True:
    succes,img = dispositivoCaputra.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    resultado = manos.process(imgRGB)

    if resultado.multi_hand_landmarks:
        for handlms in resultado.multi_hand_landmarks:
        #mpDibujar.draw_landmarks(img,handlms,mpManos.HAND_CONNECTIONS)
            for id,lm in enumerate(handlms.landmark):
                alto,ancho,color = img.shape
                cx,cy = int(lm.x*ancho),int(lm.y*alto)
                if id ==4:
                    cv2.circle(img,(cx,cy),10,(255,255,0),cv2.FILLED)
                    x4,y4 = cx,cy
                if id ==20:
                    cv2.circle(img,(cx,cy),10,(255,255,0),cv2.FILLED)
                    x20,y20 = cx,cy
            mediaX =(x4+x20)//2
            mediay = (y4+x20)//2 

            DistanciaEntreDedos = math.hypot(x20-x4,y20-y4)
            cv2.line(img,(x4,y4),(x20,y20),(0,255,0),3)

            
            if DistanciaEntreDedos<150 and cambiar == 0:
                    print("realizo accion")
                    cambiar = 1
            if DistanciaEntreDedos>290 and cambiar ==1:
                    print("paro la accion")
                    cambiar = 0
    cv2.imshow("image",img)
    cv2.waitKey(1)