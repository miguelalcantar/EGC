import pandas as pd
import keras
import os

def clasificacion(route_file):

    print('Leyendo el archivo csv')
    data = pd.read_csv(route_file)

    print('Leyendo el modelo...')
    model_name = 'best_model.h5'
    model = keras.models.load_model(f"/home/miguel/Dev/EGC/model/{model_name}")

    print('Predicciones')
    X = data[:186].values
    X = X.reshape(1, X.shape[0], 1)
    predict = model.predict(X)
    print(predict[0])

    return predict[0]
