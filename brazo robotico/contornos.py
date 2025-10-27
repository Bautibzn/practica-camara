import cv2

# Iniciar la cámara (0 = cámara principal)
cap = cv2.VideoCapture(0)

# Verificamos si se pudo abrir la cámara
if not cap.isOpened():
    print("⚠️ No se pudo acceder a la cámara.")
    exit()

while True:
    # Leer un frame de la cámara
    ret, frame = cap.read()
    if not ret:
        print("⚠️ No se pudo leer el cuadro de la cámara.")
        break

    # Convertir a escala de grises
    grises = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grises = cv2.GaussianBlur(grises, (5, 5), 0)

    # Detectar bordes con Canny
    bordes = cv2.Canny(grises, 100, 200)

    # Encontrar contornos
    contornos, jerarquia = cv2.findContours(bordes, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el frame original
    cv2.drawContours(frame, contornos, -1, (0, 0, 255), 2)

    # Mostrar cantidad de contornos
    texto = f'Contornos: {len(contornos)}'
    cv2.putText(frame, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Mostrar los resultados
    cv2.imshow('Bordes', bordes)
    cv2.imshow('Contornos en vivo', frame)

    # Presionar 's' para salir
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
