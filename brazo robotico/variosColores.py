import cv2
import numpy as np

def dibujar(frame, mask, color):
    contornos, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for c in contornos:
        area = cv2.contourArea(c)
        if area > 3000:  # filtrar ruido
            m = cv2.moments(c)
            if (m["m00"] == 0): m["m00"] = 1
            x = int(m["m10"] / m["m00"])
            y = int(m["m01"] / m["m00"])
            cv2.circle(frame, (x, y), 7, (0, 255, 0), -1)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, '{},{}'.format(x, y), (x + 10, y), font, 0.75, (0, 255, 0), 1, cv2.LINE_AA)
            nuevoContorno = cv2.convexHull(c)
            cv2.drawContours(frame, [nuevoContorno], 0, color, 3)

cap = cv2.VideoCapture(0)

# 🔵 Azul (celeste-azul fuerte)
azulbajo = np.array([95, 120, 70], np.uint8)
azulalto = np.array([130, 255, 255], np.uint8)

# 🟢 Verde (más puro, sin mezclarse con el celeste)
verdebajo = np.array([35, 120, 70], np.uint8)
verdealto = np.array([85, 255, 255], np.uint8)

# 🔴 Rojo (ajustado para luz blanca/amarilla)
rojobajo1 = np.array([0, 120, 70], np.uint8)
rojoalto1 = np.array([10, 255, 255], np.uint8)
rojobajo2 = np.array([170, 120, 70], np.uint8)
rojoalto2 = np.array([180, 255, 255], np.uint8)



while True:
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo acceder a la cámara.")
        break

    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Máscaras por color
    maskazul = cv2.inRange(frameHSV, azulbajo, azulalto)
    maskverde = cv2.inRange(frameHSV, verdebajo, verdealto)
    maskred1 = cv2.inRange(frameHSV, rojobajo1, rojoalto1)
    maskred2 = cv2.inRange(frameHSV, rojobajo2, rojoalto2)
    maskred = cv2.add(maskred1, maskred2)

    # Dibujar resultados
    dibujar(frame, maskazul, (255, 0, 0))   # Azul
    dibujar(frame, maskverde, (0, 255, 0))  # Verde
    dibujar(frame, maskred, (0, 0, 255))    # Rojo

    cv2.imshow('Detección de colores', frame)

    if cv2.waitKey(1) & 0xFF == ord('s'):  # presionar 's' para salir
        break

cap.release()
cv2.destroyAllWindows()
