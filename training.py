# importamos las librerías necesarias
import  cv2
import numpy as np
from PIL import Image
import pickle as pc
import os # Nos permite leer/escribir archivos

# Obtenemos la carpeta raíz del proyecto
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, 'img')
# Inicializamos el CascadeClassifier
cascade_classifier = cv2.CascadeClassifier('cascades/haarcascade_frontalface_alt2.xml')
# Generamos un "Reconocedor" (recognizer) para entrenar nuestro set de datos
recognizer = cv2.face.LBPHFaceRecognizer_create()
# Generar la estructura para reconocer a quien corresponder el restro
current_index = 0
labels = {} # Almacenará Key --> EDUARDOFLORES, Value --> 0
train_x = []
train_y = []
# Obtengo la raíz de la carpeta imágenes, cada uno de los folders y cada uno de los archivos
for root, dirs, files in os.walk(IMAGE_DIR):
    for file in files:
        # Itero sobre los archivos
        if file.endswith('jpg') or file.endswith('png') or file.endswith('jpeg'):
            # obtengo información básica de los archivos
            path = os.path.join(root, file)
            label = os.path.basename(root).replace(' ', '').upper()
            # Verifico si el label existe en el diccionario, caso contrario lo agrego
            if label not in labels:
                labels[label] = current_index
                current_index += 1
            # Convierto la imagen a un arreglo multidimensional
            image_pil = Image.open(path).convert('L')
            size = (500, 500)
            image = image_pil.resize(size, Image.ANTIALIAS)
            image_np = np.array(image, "uint8")
            # Ahora trabajamos con el recognizer
            face_detector = cascade_classifier.detectMultiScale(image_np, scaleFactor=1.5, minNeighbors=4)
            for (x, y, w, h) in face_detector:
                region_of_interest = image_np[y: y + h, x: x + w] # roi
                train_x.append(region_of_interest)
                train_y.append(current_index)
# Guardamos los labels a través de pickles
with open('pickles/face-labels.pickle', 'wb') as f:
    pc.dump(labels, f)
# Guardamos la data generada por el recognizer
recognizer.train(train_x, np.array(train_y))
recognizer.save('recognizers/face-trainning.yml')