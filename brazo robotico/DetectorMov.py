"""import cv2
import numpy as np

video = cv2.VideoCapture(0)
i = 0
while True:
    ret, frame = video.read()
    if ret == False: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i == 20:
        bgGray = gray
    if i > 20:
        dif = cv2.absdiff(gray, bgGray)
        _, th = cv2.threshold(dif, 40, 255, cv2.THRESH_BINARY)
        cnts, _ = cv2.findContours(th, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        #cv2.drawContours(frame, cnts, -1, (0,0,255), 2)
        #cv2.imshow('dif',dif)
        cv2.imshow('th',th)
        for c in cnts:
            area = cv2.contourArea(c)
            if area < 9000:
                x,y,w,h = cv2.boundingRect(c)
                cv2.rectangle (frame, (x,y), (x+w, y+h), (0,255,0),2)

    cv2.imshow('frame', frame)
    
    i= i+1 
    if cv2.waitKey(1) & 0xFF == ord('s'):break

video.release()
cv2.destroyAllWindows()"""

"""import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ No se pudo acceder a la cámara.")
            break

        # Convertir a RGB (requerido por MediaPipe)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        # Dibujar esqueleto si hay detección
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0,0,255), thickness=2, circle_radius=2)
            )

        cv2.imshow("Detección de Persona (MediaPipe Pose)", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

cap.release()
cv2.destroyAllWindows()"""

"""from ultralytics import YOLO
import cv2

# Cargar modelo preentrenado (detecta personas, autos, etc.)
modelo = YOLO("yolov8n.pt")  # 'n' = nano (liviano y rápido)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detección
    resultados = modelo(frame, stream=True)

    for r in resultados:
        for box in r.boxes:
            # Obtener clase (por ejemplo, 'person')
            clase = int(box.cls[0])
            nombre = modelo.names[clase]

            if nombre == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, "Persona", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    cv2.imshow("Detección de Personas (YOLOv8)", frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()"""

