import cv2

dispositivo = cv2.VideoCapture(0)  # Cambiá el 0 si es otro

if not dispositivo.isOpened():
    print("❌ No se pudo acceder a la cámara.")
    exit()

# Opcional: ajustar resolución
dispositivo.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
dispositivo.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    bien, img = dispositivo.read()
    if not bien:
        print("⚠️ No se pudo leer el frame.")
        break

    cv2.imshow("Camara Notebook", img)

    if cv2.waitKey(1) & 0xFF == 27:  # Presionar ESC para salir
        break

dispositivo.release()
cv2.destroyAllWindows()
