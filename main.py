# Importamos las librerías para levantar la app
import numpy as np
import cv2
import pickle as pc

# Inicializamos el CascadeClassifier
cascade_classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
# Inicializamos y cargamos nuestro recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizers/face-trainning.yml')
# Obtenemos los labels
labels = {}
with open('pickles/face-labels.pickle', 'rb') as f:
    labels_bites = pc.load(f)
    labels = { key:value for value, key in labels_bites.items()}
# Capturamos el vídeo desde nuestra cámara
capture = cv2.VideoCapture(0+cv2.CAP_DSHOW)
while(True):
    ret, frame = capture.read()
    # Ahora procesaremos la imagen para usar escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Habilitamos el clasificador como hicimos en el training
    face_detector = cascade_classifier.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=4)
    # Recorremos los resultados y obtenemos la Región de Interés
    for (x, y, w, h) in face_detector:
        region_of_interest = gray[y: y + h, x: x + w] # roi
        roi_color = frame[y: y + h, x: x + w]
        label_id, confidence = recognizer.predict(region_of_interest)
        if confidence > 4 and confidence <= 99:
            # Defino los parámetros de dibujo sobre el frame
            font = cv2.FONT_HERSHEY_SIMPLEX
            name_of_picture = labels[label_id - 1]
            # print(f"{labels[label_id - 1]} --> {confidence}")
            color = (255, 255, 255)
            stroke = 1
            # Dibujo el texto sobre el frame
            cv2.putText(frame, name_of_picture, (x, y), font, 1, color, stroke, cv2.LINE_AA)
            # Ahora enmaracamos el rostro con un rectángulo
        color_line = (28, 28, 191)
        stroke_line = 1
        x_end = x + w
        y_end = y + h
        cv2.rectangle(frame, (x, y), (x_end, y_end), color_line, stroke_line)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Detector Algorítmica Avanzada', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
# Liberamos el proceso que maneja la cámara
capture.release()
# Cerramos todas las ventanas disponibles
cv2.destroyAllWindows()