import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from flask import jsonify
retina_model = load_model('static/models/retina_model.h5')
Report_FOLDER = 'static/RetinaUpload/'
Temp_FOLDER = 'static/Temp'


def ProcessRetina(IMG):
    # Read image
    data = image.load_img(IMG, target_size=(130, 130, 3),)
    data = np.expand_dims(data, axis=0)
    data = data * 1.0 / 255

    result = retina_model.predict(data)
    indices = {0: 'Infected', 1: 'Uninfected'}
    predictioned_class = np.asscalar(np.argmax(result, axis=1))
    accuracy = round(result[0][predictioned_class] * 100, 2)
    accuracy = float(accuracy)
    prediction = indices[predictioned_class]

    predict = {
        "RU_prediction": prediction,
        "RU_accuracy": accuracy
        }

    return predict
    #res = model.prediction(image)
