# Primero importar las librerías 
import numpy as np
import cv2
# Capturamos el vídeo desde nuestra cámara
capture = cv2.VideoCapture(0+cv2.CAP_DSHOW)
while(True):
    ret, frame = capture.read()
    # Mostramos lo que capturamos en una ventana
    cv2.imshow('frame', frame)
    # Ahora procesaremos la imagen para usar escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray)
    # Ahora utilizaremos 
    random = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)
    cv2.imshow('random', random)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# Liberamos el proceso que maneja la cámara
capture.release()
# Cerramos todas las ventanas disponibles
cv2.destroyAllWindows()