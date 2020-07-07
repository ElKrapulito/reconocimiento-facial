import pandas as pd
import numpy as np
from PIL import Image
# ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
df = pd.read_csv('csv/fer2013.csv')
# print(df.head())
pix = df[['emotion','pixels']]
cont = 0
for emo, pixelitos in pix.iterrows():
    arr = np.fromstring(pixelitos['pixels'], dtype=np.uint8, sep=' ')
    img = Image.fromarray(arr.reshape(48,48))
    if pixelitos['emotion'] == 1: 
        img.save(f'img/Asco/test{cont}.png')
    elif pixelitos['emotion'] == 2:
        img.save(f'img/Miedo/test{cont}.png')
    elif pixelitos['emotion'] == 3:
        img.save(f'img/Feliz/test{cont}.png')
    elif pixelitos['emotion'] == 4:
        img.save(f'img/Triste/test{cont}.png')
    elif pixelitos['emotion'] == 5:
        img.save(f'img/Sorpresa/test{cont}.png')
    elif pixelitos['emotion'] == 6:
        img.save(f'img/Neutro/test{cont}.png')
    cont = cont + 1
