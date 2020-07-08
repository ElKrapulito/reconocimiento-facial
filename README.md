# Reconocimiento facial

Primero instalar requierments, luego se tiene que descargar le csv y ponerlo dentro de una carpeta llamada [**csv**](https://drive.google.com/file/d/156FQlEyBkAQ58FvU5C2jCZ824oBwq1z-/view?usp=sharing), 
despues una ves tenemos el csv con los datos de las imagenes se tiene que crear la carpeta **img** para guardar las imagenes
de entrenamiento en las cuales tienen que ir las siguientes carpetas de sentimientos:
- Asco
- Enojado
- Feliz
- Miedo
- Neutro
- Sorpresa
- Triste

Despues crear una las carpetas:
- recognizers
- pickles
- images

Recognizer y pickles son para los datos de entrenamiento y luego la images son para las imagenes que se usaran de ejemplos.
Luego correr el archivo de **traininig.py** para generar los archivos necesarios para correr la red **El entrenamiento tarda aproximadamente 10min dependiendo del sistema**, luego se puede correr el archivo **gui.py** para probar el programa.
