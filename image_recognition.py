from azure.cognitiveservices.vision.customvision.training import training_api
from azure.cognitiveservices.vision.customvision.training.models import ImageUrlCreateEntry

from azure.cognitiveservices.vision.customvision.prediction import prediction_endpoint

from azure.cognitiveservices.vision.customvision.prediction.prediction_endpoint import models

import os

import requests

import string

def identify(image):

    predictor = prediction_endpoint.PredictionEndpoint("15c7f6bd782b4fab887295c83a608f42")
    with open(image, mode="rb") as test_data:
        results = predictor.predict_image("ac4d0722-29ce-4116-b9d2-225b453a3df3", test_data.read())
    answer = None
    percent = 0
    for prediction in results.predictions:
        if prediction.probability > .5: 
            if (answer == None):
                answer = prediction.tag
            else:
                if prediction.probability > percent:
                    answer = prediction.tag
                    percent = prediction.probability
    return answer

#takes in a list of paths to photos including row/col index
def images2Circ(photos):
    rows = 6
    cols = 8
    circuit = [[None for i in range(cols)] for j in range(rows)]
    for pic in photos:
        row = int(pic[10])
        col = int(pic[12])
        print(row,col)
        gate = identify(pic)
        circuit[row][col] = gate
    return circuit


print(images2Circ(["pic/t3/aaa2a3.jpg","pic/t3/bbb1b4.jpg","pic/t3/ccc5c2.jpg","pic/t3/ddd5d5.jpg","pic/t3/eee0e0.jpg"]))
        
        
