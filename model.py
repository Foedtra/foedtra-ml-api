import json
import os
import tensorflow as tf
from PIL import Image
import urllib.request
from keras_preprocessing import image
from keras.models import load_model


class Model:
    def __init__(self, model_path=os.path.join(os.getcwd(), 'model')):
        self.model_path = model_path

    def _load_model(self):
        return load_model(self.model_path)

    def _normalizeImage(self, img):
        img = tf.keras.preprocessing.image.smart_resize(img, (224, 224))
        img = image.img_to_array(img)
        img = tf.expand_dims(img, axis=0)

        return img / 255

    def _load_json(self):
        dataset = json.load(open('dataframe-traditional-food.json', 'r'))
        for data in dataset['data']:
            data['keyword'] = data['namaMakanan'].lower().replace(' ', '_')
    
        return dataset


    def predict(self, image):
        dataset = self._load_json()
        model = self._load_model()
        urllib.request.urlretrieve(image, 'image.jpg')
        img = Image.open('image.jpg')
        img = self._normalizeImage(img)
        predictions = model.predict(img)
        predictions = tf.argmax(predictions[0])  
        prediction = dataset['data'][predictions]
        os.remove('image.jpg')
        return prediction
    

